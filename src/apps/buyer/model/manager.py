from typing import Any
from django.db import models

from apps.common.models import User


class BuyerManager(models.Manager):
    """
    Manager для модели Buyer, который переопределяет логику создания объекта Buyer.
    """

    def create(self, user_id, **kwargs: Any) -> Any:
        user = User.objects.get(id=user_id)
        return super().create(user=user, **kwargs)
