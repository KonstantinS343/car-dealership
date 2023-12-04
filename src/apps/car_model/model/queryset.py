from django.db import models

from django.db.models import Manager


class CarQuerySet(models.QuerySet):
    """
    QuerySet класс, который фильтрует Car модель.
    """

    def cars(self) -> Manager[models.Model]:
        return self.filter(is_active=True)
