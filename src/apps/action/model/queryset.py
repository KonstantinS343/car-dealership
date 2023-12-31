from django.db import models

from django.db.models import Manager


class ActionQuerySet(models.QuerySet):
    """
    QuerySet класс, который фильтрует ActionCarDealership, ActionSupplier модель.
    """

    def action_carshow(self) -> Manager[models.Model]:
        return self.filter(is_active=True).select_related('car_dealership', 'car_model')

    def action_supplier(self) -> Manager[models.Model]:
        return self.filter(is_active=True).select_related('supplier', 'car_model')

    def get_action_by_car_supplier(self, supplier, car_model) -> Manager[models.Model]:
        return self.filter(supplier=supplier, car_model=car_model)

    def get_action_by_car_carshow(self, carshow, car_model) -> Manager[models.Model]:
        return self.filter(car_dealership=carshow, car_model=car_model)
