from django.core.management.base import BaseCommand
from django.db import transaction

import random

from apps.buyer.model.models import Buyer
from apps.car_model.model.models import Car
from apps.car_show.model.models import CarShow, UniqueBuyersCarDealership
from apps.common.models import User
from apps.supplier.model.models import Supplier, SupplierCarModel, UniqueBuyersSuppliers
from apps.purchase_history.model.models import PurchasesSalesHistorySupplier, PurchasesSalesHistoryСarShow


def gen_float(a: float, b: float, precision: int = 2) -> float:
    return round(random.uniform(a, b), precision)


class Command(BaseCommand):
    """
    Класс, который реализует команду заполнения базы данных.
    Создается клиентов - 10, поставщиков - 10, автосалонов - 5, автомобилей - 50,
    уникальных клиентов автосалона - 5, уникальных клиентов поставщиков - 4,
    продажи всех поставщиков - 20, продажи всех автосалонов - 20, покупки всех клиентов - 20.
    """

    help = 'Command to populate the database'
    CAR_BRANDS = ('BMW', 'Hyundai', 'Honda', 'Ford', 'Audi', 'Volkswagen', 'Mercedes-Benz')

    def gen_user(self) -> None:
        """
        Функция создание пользователей, покупателей, поставщиков.
        """
        self.suppliers_list = []
        self.buyer_list = []
        for i in range(10):
            buyer_user = User.objects.create_user(username=f'client_{i}', password='password', user_type=1, email_confirmed=True)
            supplier_user = User.objects.create_user(username=f'supplier_{i}', password='password', user_type=3, email_confirmed=True)
            supplier = Supplier.objects.create(user_id=supplier_user.id, name='Supplier Name', country='RU', year_foundation=1990, buyer_amount=100)
            buyer = Buyer.objects.create(user_id=buyer_user.id, balance=gen_float(100000.0, 1000000.0))
            self.suppliers_list.append(supplier)
            self.buyer_list.append(buyer)

    def gen_carshow(self) -> None:
        """
        Функция создание автосалонов.
        """
        self.cars_specifications = []
        self.carshow_list = []
        for i in range(5):
            carshow_user = User.objects.create_user(username=f'carshow_owner_{i}', password='password', user_type=2, email_confirmed=True)
            self.cars_specifications.append(
                {
                    'weight': gen_float(0.5, 10.0),
                    'engine_capacity': gen_float(1.0, 8.0, 1),
                    'fuel_type': random.choice(CarShow.FUEL_TYPE)[0],
                    'gearbox_type': random.choice(CarShow.GEARBOX_TYPE)[0],
                    'car_body': random.choice(CarShow.CAR_BODY_TYPE)[0],
                }
            )
            carshow = CarShow.objects.create(
                user_id=carshow_user.id, name=f'Car Show Name {i}', country='RU', balance=gen_float(1000000.0, 20000000.0), **self.cars_specifications[-1]
            )
            self.carshow_list.append(carshow)

    def gen_cars(self) -> None:
        """
        Функция создания автомобилей и распредление автомобилей.
        """
        self.car_list = []
        for i in range(50):
            car = Car.objects.create(brand=random.choice(Command.CAR_BRANDS), **random.choice(self.cars_specifications))
            SupplierCarModel.objects.create(supplier=random.choice(self.suppliers_list), car_model=car, price=gen_float(30000.0, 200000.0))
            self.car_list.append(car)

    def gen_unique_buyers_carshow(self) -> None:
        """
        Функция для генерации постоянных клиентов автосалона.
        """
        for i in range(5):
            UniqueBuyersCarDealership.objects.create(car_dealership=random.choice(self.carshow_list), buyer=random.choice(self.buyer_list))

    def gen_unique_buyers_supplier(self) -> None:
        """
        Функция для генерации постоянных клиентов поставщика.
        """
        for i in range(4):
            UniqueBuyersSuppliers.objects.create(car_dealership=random.choice(self.carshow_list), supplier=random.choice(self.suppliers_list))

    def gen_history_buyer_carshow(self) -> None:
        """
        Функция для генерации истории продаж автосалонов и истории покупок покупетелей.
        """
        for i in range(20):
            PurchasesSalesHistoryСarShow.objects.create(
                buyer=random.choice(self.buyer_list),
                car_dealership=random.choice(self.carshow_list),
                car_model=random.choice(self.car_list),
                final_price=gen_float(30000.0, 200000.0),
            )

    def gen_history_buyer_supplier(self) -> None:
        """
        Функция для генерации истории продаж поставщиков.
        """
        for i in range(20):
            PurchasesSalesHistorySupplier.objects.create(
                supplier=random.choice(self.suppliers_list),
                car_dealership=random.choice(self.carshow_list),
                car_model=random.choice(self.car_list),
                final_price=gen_float(30000.0, 200000.0),
            )

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.gen_user()
        self.gen_carshow()
        self.gen_cars()
        self.gen_unique_buyers_carshow()
        self.gen_unique_buyers_supplier()
        self.gen_history_buyer_carshow()
        self.gen_history_buyer_supplier()
