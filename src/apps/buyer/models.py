from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

import uuid


class Buyer(AbstractUser):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Время обновления"))

    def __str__(self) -> str:
        return super().username

    class Meta:
        verbose_name = _("Покупатель")
        verbose_name_plural = _("Покупатели")
