from django.db import models

from typing import List

from django.db.models import Manager


class CarShowQuerySet(models.QuerySet):
    """
    QuerySet класс, который фильтрует CarShow, CarShowModel, UniqueBuyersCarDealership, CarDealershipSuppliersList модель.
    """

    def get_carshow_by_user_id(self, user) -> Manager[models.Model]:
        return self.filter(user=user, is_active=True)

    def get_carshow_by_id(self, id) -> Manager[models.Model]:
        return self.filter(car_dealership_id=id, is_active=True).select_related('car_model', 'car_dealership')

    def get_carshow_by_id_unique_buyer(self, id) -> Manager[models.Model]:
        return self.filter(car_dealership_id=id, is_active=True).select_related('buyer__user', 'car_dealership')

    def get_carshow_by_id_supplier_list(self, id) -> Manager[models.Model]:
        return self.filter(car_dealership_id=id, is_active=True).select_related('supplier', 'car_dealership')

    def get_all_active_carshow(self) -> Manager[models.Model]:
        return self.filter(user__email_confirmed=True, is_active=True)

    def get_supplier_from_supplier_list(self, carshow) -> Manager[models.Model]:
        return self.filter(car_dealership=carshow, is_active=True)

    def get_unique_buyer(self, buyer) -> Manager[models.Model]:
        return self.filter(buyer=buyer, is_active=True)

    def get_car_with_lowest_price(self, specification, carshow=None) -> List[Manager[models.Model]]:
        filter_kwargs = {
            'car_model__fuel_type': specification["fuel_type"],
            'car_model__gearbox_type': specification["gearbox_type"],
            'car_model__car_body': specification["car_body"],
            'model_amount__gt': 0,
        }
        if carshow:
            filter_kwargs['car_dealership'] = carshow
        return self.filter(**filter_kwargs).order_by('price').first()
