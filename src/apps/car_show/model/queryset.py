from django.db import models

from django.db.models import Manager


class CarShowQuerySet(models.QuerySet):
    """
    QuerySet класс, который фильтрует CarShow, CarShowModel, UniqueBuyersCarDealership, CarDealershipSuppliersList модель.
    """

    def get_carshow_by_user_id(self, user) -> Manager[models.Model]:
        return self.filter(user=user, is_active=True)

    def get_carshow_by_id(self, id) -> Manager[models.Model]:
        return self.filter(car_dealership_id=id, is_active=True)
