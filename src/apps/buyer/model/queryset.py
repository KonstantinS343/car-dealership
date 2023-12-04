from django.db import models

from django.db.models import Manager


class BuyerQuerySet(models.QuerySet):
    """
    QuerySet класс, который фильтрует Buyer модель.
    """

    def get_buyer_by_user_id(self, user_id) -> Manager[models.Model]:
        return self.filter(user_id=user_id, is_active=True)