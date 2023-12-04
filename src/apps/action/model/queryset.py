from django.db import models

from django.db.models import Manager


class ActionQuerySet(models.QuerySet):
    """
    QuerySet класс, который фильтрует ActionCarDealership, ActionSupplier модель.
    """

    def actions(self) -> Manager[models.Model]:
        return self.filter(is_active=True)
