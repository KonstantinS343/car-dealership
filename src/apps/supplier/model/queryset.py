from django.db import models

from django.db.models import Manager

from typing import List


class SupplierQuerySet(models.QuerySet):
    """
    QuerySet класс, который фильтрует Supplier, UniqueBuyersSuppliers, SupplierCarModel модель.
    """

    def get_supplier_by_id(self, supplier) -> Manager[models.Model]:
        return self.filter(supplier_id=supplier, is_active=True)

    def get_supplier_by_user_id(self, user) -> Manager[models.Model]:
        return self.filter(user_id=user, is_active=True)

    def get_car_with_lowest_price(self, specification, brand, supplier=None) -> List[Manager[models.Model]]:
        filter_kwargs = {
            'car_model__brand': brand,
            'car_model__weight': specification["weight"],
            'car_model__engine_capacity': specification["engine_capacity"],
            'car_model__fuel_type': specification["fuel_type"],
            'car_model__gearbox_type': specification["gearbox_type"],
            'car_model__car_body': specification["car_body"],
        }
        if supplier:
            filter_kwargs['supplier'] = supplier
        return self.filter(**filter_kwargs).order_by('price').first()

    def get_unique_suppliers_carshow(self, carshow) -> List[Manager[models.Model]]:
        return [i.supplier for i in self.filter(car_dealership=carshow)]
