from django.core.management.base import BaseCommand

from django.utils import timezone

from apps.action.model.models import ActionCarDealership, ActionSupplier
from apps.buyer.model.models import Buyer
from apps.car_model.model.models import Car
from apps.car_show.model.models import CarShow, CarShowModel, CarDealershipSuppliersList, UniqueBuyersCarDealership
from apps.common.models import User
from apps.purchase_history.model.models import PurchasesSalesHistorySupplier, PurchasesSalesHistoryСarShow
from apps.supplier.model.models import Supplier, SupplierCarModel, UniqueBuyersSuppliers


class Command(BaseCommand):
    help = 'Command to populate the database'

    def handle(self, *args, **kwargs):
        buyer_user = User.objects.create(username='client', password='password', user_type=1, email_confirmed=True)
        carshow_user = User.objects.create(username='carshow_owner', password='password', user_type=2, email_confirmed=True)
        supplier_user = User.objects.create(username='supplier', password='password', user_type=3, email_confirmed=True)
        supplier = Supplier.objects.create(user_id=supplier_user.id, name='Supplier Name', country='RU', year_foundation=1990, buyer_amount=100)
        carshow = CarShow.objects.create(
            user=carshow_user,
            name='Car Show Name',
            country='RU',
            balance=10000.00,
            weight=1.5,
            engine_capacity=2.0,
            fuel_type='Petrol',
            gearbox_type='Automatic',
            car_body='Sedan',
        )
        buyer = Buyer.objects.create(user=buyer_user, balance=0.0)
        car = Car.objects.create(brand='brand', weight=1.0, engine_capacity=2.0, fuel_type='Petrol', gearbox_type='Mechanical', car_body='Sedan')
        CarShowModel.objects.create(car_dealership=carshow, car_model=car, model_amount=10)
        UniqueBuyersCarDealership.objects.create(car_dealership=carshow, buyer=buyer)
        CarDealershipSuppliersList.objects.create(car_dealership=carshow, supplier=supplier)
        SupplierCarModel.objects.create(supplier=supplier, car_model=car, price=1000.0)
        UniqueBuyersSuppliers.objects.create(car_dealership=carshow, supplier=supplier)
        PurchasesSalesHistorySupplier.objects.create(supplier=supplier, car_dealership=carshow, car_model=car, final_price=1000.0)
        PurchasesSalesHistoryСarShow.objects.create(buyer=buyer, car_dealership=carshow, car_model=car, final_price=1000.0)
        ActionCarDealership.objects.create(
            name="Название акции",
            descritpion="Описание",
            event_start=timezone.now().date(),
            event_end=timezone.now().date() + timezone.timedelta(days=10),
            discount=0.1,
            car_dealership=carshow,
            car_model=car,
        )
        ActionSupplier.objects.create(
            name="Название акции",
            descritpion="Описание",
            event_start=timezone.now().date(),
            event_end=timezone.now().date() + timezone.timedelta(days=10),
            discount=0.1,
            supplier=supplier,
            car_model=car,
        )
