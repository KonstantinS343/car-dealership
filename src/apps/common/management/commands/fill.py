from django.core.management.base import BaseCommand
from django.db import transaction

import random
from typing import List, Dict, Tuple, Any

from apps.buyer.model.models import Buyer
from apps.car_model.model.models import Car
from apps.car_show.model.models import CarShow, UniqueBuyersCarDealership
from apps.common.models import User
from apps.supplier.model.models import Supplier, SupplierCarModel


def gen_float(a: float, b: float, precision: int = 2) -> float:
    return round(random.uniform(a, b), precision)


class Command(BaseCommand):
    """
    Класс, который реализует команду заполнения базы данных.
    Создается клиентов - 10, поставщиков - 10, автосалонов - 5, автомобилей - 50.
    """

    help = 'Command to populate the database'
    CAR_BRANDS = ('BMW', 'Hyundai', 'Honda', 'Ford', 'Audi', 'Volkswagen', 'Mercedes-Benz')

    @staticmethod
    def gen_user() -> Tuple[List[Supplier], List[Buyer]]:
        """
        Функция создание пользователей, покупателей, поставщиков.
        """
        suppliers_list = []
        buyer_list = []
        for i in range(10):
            buyer_user = User.objects.create_user(username=f'client_{i}', password='password', user_type=1, email_confirmed=True)
            supplier_user = User.objects.create_user(username=f'supplier_{i}', password='password', user_type=3, email_confirmed=True)
            supplier = Supplier.objects.create(user_id=supplier_user.id, name='Supplier Name', country='RU', year_foundation=1990, buyer_amount=100)
            buyer = Buyer.objects.create(user_id=buyer_user.id, balance=gen_float(100000.0, 1000000.0))
            suppliers_list.append(supplier)
            buyer_list.append(buyer)
        return suppliers_list, buyer_list

    @staticmethod
    def gen_carshow() -> Tuple[List[Dict[str, Any]], List[CarShow]]:
        """
        Функция создание автосалонов.
        """
        cars_specifications = []
        carshow_list = []
        for i in range(5):
            carshow_user = User.objects.create_user(username=f'carshow_owner_{i}', password='password', user_type=2, email_confirmed=True)
            cars_specifications.append(
                {
                    'weight': gen_float(0.5, 10.0),
                    'engine_capacity': gen_float(1.0, 8.0, 1),
                    'fuel_type': random.choice(CarShow.FUEL_TYPE)[0],
                    'gearbox_type': random.choice(CarShow.GEARBOX_TYPE)[0],
                    'car_body': random.choice(CarShow.CAR_BODY_TYPE)[0],
                }
            )
            carshow = CarShow.objects.create(
                user_id=carshow_user.id, name=f'Car Show Name {i}', country='RU', balance=gen_float(1000000.0, 20000000.0), **cars_specifications[-1]
            )
            carshow_list.append(carshow)
        return cars_specifications, carshow_list

    @staticmethod
    def gen_cars(cars_specifications: List[Dict[str, str | float]], suppliers: List[Supplier]) -> None:
        """
        Функция создания автомобилей и распредление автомобилей.
        """
        for i in range(50):
            car = Car.objects.create(brand=random.choice(Command.CAR_BRANDS), **random.choice(cars_specifications))
            SupplierCarModel.objects.create(supplier=random.choice(suppliers), car_model=car, price=gen_float(30000.0, 200000.0))

    @staticmethod
    def gen_unique_buyers(buyers: List[Buyer], carshows: List[CarShow]) -> None:
        """
        Функция для генерации постоянных клиентов автосална.
        """
        for i in range(5):
            UniqueBuyersCarDealership.objects.create(car_dealership=random.choice(carshows), buyer=random.choice(buyers))

    @transaction.atomic
    def handle(self, *args, **kwargs):
        suppliers, buyers = Command.gen_user()
        cars_specifications, carshows = Command.gen_carshow()
        Command.gen_cars(cars_specifications=cars_specifications, suppliers=suppliers)
        Command.gen_unique_buyers(buyers=buyers, carshows=carshows)
