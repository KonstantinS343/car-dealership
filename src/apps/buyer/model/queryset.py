from django.db import models

from django.db.models import Manager


class BuyerQuerySet(models.QuerySet):
    """
    QuerySet класс, который фильтрует Buyer модель.
    """

    def for_buyer(self, user) -> Manager[models.Model]:
        return self.filter(user=user, is_active=True)
