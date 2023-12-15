from celery import shared_task

from django.utils import timezone
from decimal import Decimal

from apps.car_show.model.models import CarShow, CarDealershipSuppliersList, CarShowModel
from apps.purchase_history.model.models import PurchasesSalesHistoryСarShow, PurchasesSalesHistorySupplier
from apps.supplier.model.models import SupplierCarModel
from apps.action.model.models import ActionSupplier

REGULAR_CUSTOMER_DISCOUNT = Decimal(0.8)
EXTRA_CHARGE = Decimal(0.2)


@shared_task
def carshow_buy_car():
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
        cars_for_buy = []
        for j in reqular_supplier.iterator():
            car = SupplierCarModel.objects.get_car_with_lowest_price(
                specification=specification, brand=most_popular_car[0]['car_model__brand'], supplier=j.supplier
            )
            if car:
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
                    shop_car[0].count += 1
                shop_car[0].price = new_price
                shop_car[0].save()

                shop.save()

                PurchasesSalesHistorySupplier.objects.create(
                    supplier=car_for_buy.supplier, car_dealership=shop, car_model=car_for_buy.car_model, final_price=new_price
                )

                print(f'Car Dealership {shop.name} BUY {car_for_buy.car_model.brand} PRICE {car_for_buy.price} NEW PRICE {new_price}')
