from celery import shared_task

from django.utils import timezone
from decimal import Decimal

from typing import NamedTuple, Dict
import random

from apps.car_show.model.models import CarShow, CarDealershipSuppliersList, CarShowModel, UniqueBuyersCarDealership
from apps.purchase_history.model.models import PurchasesSalesHistoryСarShow, PurchasesSalesHistorySupplier
from apps.supplier.model.models import SupplierCarModel, UniqueBuyersSuppliers
from apps.action.model.models import ActionSupplier, ActionCarDealership
from apps.buyer.model.models import Buyer

REGULAR_CUSTOMER_DISCOUNT = Decimal(0.8)
EXTRA_CHARGE = Decimal(0.2)


class Offer(NamedTuple):
    specification: Dict[str, str | float]
    max_price: Decimal


@shared_task
def carshow_buy_car():
    """
    Скрипт покупки авто у поставщиков.
    """
    shops = CarShow.objects.get_all_active_carshow()
    most_popular_car = PurchasesSalesHistoryСarShow.objects.get_popular_car_brand()

    for shop in shops.iterator():
        specification = {
            'weight': shop.weight,
            'engine_capacity': shop.engine_capacity,
            'fuel_type': shop.fuel_type,
            'gearbox_type': shop.gearbox_type,
            'car_body': shop.car_body,
        }
        reqular_supplier = CarDealershipSuppliersList.objects.get_supplier_from_supplier_list(carshow=shop)
        suppliers_unique_shop = UniqueBuyersSuppliers.objects.get_unique_suppliers_carshow(carshow=shop)
        cars_for_buy = []
        for j in reqular_supplier.iterator():
            car = SupplierCarModel.objects.get_car_with_lowest_price(
                specification=specification, brand=most_popular_car[0]['car_model__brand'], supplier=j.supplier
            )
            if car and car.supplier in suppliers_unique_shop:
                car.price *= REGULAR_CUSTOMER_DISCOUNT  # скидка постоянного покупателя
                cars_for_buy.append(car)
        supplier_car = SupplierCarModel.objects.get_car_with_lowest_price(specification=specification, brand=most_popular_car[0]['car_model__brand'])
        if supplier_car:
            cars_for_buy.append(supplier_car)
        for item in cars_for_buy:
            action = ActionSupplier.objects.get_action_by_car_supplier(supplier=item.supplier, car_model=item.car_model)
            if action:
                action = sorted(action, key=lambda x: x.discount, reverse=True)
                for j in action:
                    today = timezone.now().date()
                    if today > j.event_start and today < j.event_end:
                        item.price *= 1 - j.discount

        try:
            car_for_buy = sorted(cars_for_buy, key=lambda x: x.price)[0]
        except IndexError:
            continue
        else:
            if shop.balance > car_for_buy.price:
                shop.balance -= car_for_buy.price
                new_price = car_for_buy.price + (EXTRA_CHARGE * car_for_buy.price)
                shop_car = CarShowModel.objects.update_or_create(car_dealership=shop, car_model=car_for_buy.car_model)
                if not shop_car[1]:
                    shop_car[0].model_amount += 1
                shop_car[0].price = new_price
                shop_car[0].save()

                shop.save()

                PurchasesSalesHistorySupplier.objects.create(
                    supplier=car_for_buy.supplier, car_dealership=shop, car_model=car_for_buy.car_model, final_price=new_price
                )

                purchase_amount = len(PurchasesSalesHistorySupplier.objects.get_amount_carshow_buying(id=shop.id))

                if purchase_amount > 10:
                    UniqueBuyersSuppliers.objects.create(car_dealership=shop, supplier=car_for_buy.supplier)

                print(
                    f'Car Dealership {shop.name} BUY {car_for_buy.car_model.brand} ID {car_for_buy.car_model.id} PRICE {car_for_buy.price} NEW PRICE {new_price}'
                )


@shared_task
def buyer_buy_car():
    """
    Скрипт покупки авто у автосалонов.
    """
    clients = Buyer.objects.get_all_active_buyer()

    for client in clients.iterator():
        max_price = round(random.uniform(30000.0, 200000.0), 2)
        while max_price > client.balance:
            max_price = round(random.uniform(30000.0, 200000.0), 2)

        offer = Offer(
            specification={
                'fuel_type': random.choice(CarShow.FUEL_TYPE)[0],
                'gearbox_type': random.choice(CarShow.GEARBOX_TYPE)[0],
                'car_body': random.choice(CarShow.CAR_BODY_TYPE)[0],
            },
            max_price=Decimal(max_price),
        )
        reqular_clients = UniqueBuyersCarDealership.objects.get_unique_buyer(buyer=client)
        cars_for_buy = []
        for j in reqular_clients.iterator():
            car = CarShowModel.objects.get_car_with_lowest_price(specification=offer.specification, carshow=j.car_dealership)
            if car:
                car.price *= REGULAR_CUSTOMER_DISCOUNT  # скидка постоянного покупателя
                if car.price < offer.max_price:
                    cars_for_buy.append(car)
        carshow_car = CarShowModel.objects.get_car_with_lowest_price(specification=offer.specification)
        if carshow_car:
            if carshow_car.price < offer.max_price:
                cars_for_buy.append(carshow_car)
        for item in cars_for_buy:
            action = ActionCarDealership.objects.get_action_by_car_carshow(carshow=item.car_dealership, car_model=item.car_model)
            if action:
                action = sorted(action, key=lambda x: x.discount, reverse=True)
                for j in action:
                    today = timezone.now().date()
                    if today > j.event_start and today < j.event_end:
                        item.price *= 1 - j.discount

        try:
            car_for_buy = sorted(cars_for_buy, key=lambda x: x.price)[0]
        except IndexError:
            continue
        else:
            client.balance -= car_for_buy.price
            shop_car = car_for_buy
            shop_car.model_amount -= 1
            shop_car.save()
            client.save()
            PurchasesSalesHistoryСarShow.objects.create(
                car_dealership=shop_car.car_dealership, buyer=client, car_model=car_for_buy.car_model, final_price=car_for_buy.price
            )
            purchase_amount = len(PurchasesSalesHistoryСarShow.objects.get_amount_buyer_buying(id=client.id))

            if purchase_amount > 10:
                UniqueBuyersCarDealership.objects.create(car_dealership=shop_car.car_dealership, buyer=client)
            print(f'Buyer {client.user.username} BUY {car_for_buy.car_model.brand} PRICE {car_for_buy.price}')


@shared_task
def check_supplier_list():
    """
    Скрипт проверки списка поставщиков автосалона.
    """
    shops = CarShow.objects.get_all_active_carshow()

    for shop in shops.iterator():
        specification = {
            'weight': shop.weight,
            'engine_capacity': shop.engine_capacity,
            'fuel_type': shop.fuel_type,
            'gearbox_type': shop.gearbox_type,
            'car_body': shop.car_body,
        }
        reqular_supplier = CarDealershipSuppliersList.objects.get_supplier_from_supplier_list(carshow=shop)
        suppliers_unique_shop = UniqueBuyersSuppliers.objects.get_unique_suppliers_carshow(carshow=shop)
        cars_for_buy = []
        for j in reqular_supplier.iterator():
            car = SupplierCarModel.objects.get_car_with_lowest_price(specification=specification, supplier=j.supplier)
            if car and car.supplier in suppliers_unique_shop:
                car.price *= REGULAR_CUSTOMER_DISCOUNT  # скидка постоянного покупателя
                cars_for_buy.append(car)
        supplier_car = SupplierCarModel.objects.get_car_with_lowest_price(specification=specification)
        if supplier_car:
            cars_for_buy.append(supplier_car)

        for item in cars_for_buy:
            action = ActionSupplier.objects.get_action_by_car_supplier(supplier=item.supplier, car_model=item.car_model)
            if action:
                action = sorted(action, key=lambda x: x.discount, reverse=True)
                for j in action:
                    today = timezone.now().date()
                    if today > j.event_start and today < j.event_end:
                        item.price *= 1 - j.discount

        cars_for_buy = sorted(cars_for_buy, key=lambda x: x.price)
        try:
            best_car_offer = cars_for_buy[0]
            suppliers_list = [i.supplier for i in reqular_supplier]
            if best_car_offer.supplier not in suppliers_list:
                CarDealershipSuppliersList.objects.create(car_dealership=shop, supplier=best_car_offer.supplier)
                print(f'Car Dealership {shop.name} ADD NEW SUPPLIER {best_car_offer.supplier}')
            worst_car_offer = cars_for_buy[-1]
            if worst_car_offer.supplier in suppliers_list and worst_car_offer != best_car_offer and len(cars_for_buy) > 2:
                CarDealershipSuppliersList.objects.get(car_dealership=shop, supplier=worst_car_offer.supplier).delete()
                print(f'Car Dealership {shop.name} DELETE SUPPLIER {worst_car_offer.supplier}')
        except IndexError:
            continue
