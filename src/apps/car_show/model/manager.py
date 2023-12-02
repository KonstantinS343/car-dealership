from typing import Any
from django.db import models

from apps.common.models import User


class CarShowManager(models.Manager):
    """
    Manager для модели CarShow, который переопределяет логику создания объекта Supplier.
    """

    def create(self, user_id, **kwargs: Any) -> Any:
        user = User.objects.get(id=user_id)
        return super().create(user=user, **kwargs)
