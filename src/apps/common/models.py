from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid


class TimeStampedUUIDModel(models.Model):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Время создания"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Время обновления"))
    is_active = models.BooleanField(_("Активный"), default=True)

    class Meta:
        abstract = True
