from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser

import uuid


class TimeStampedUUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Время создания"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Время обновления"))
    is_active = models.BooleanField(_("Активный"), default=True)

    def delete(self) -> None:
        self.is_active = False
        self.save()

    class Meta:
        abstract = True


class User(AbstractUser):
    USER_TYPE = [
        (0, _('Неизвестный')),
        (1, _('Покупатель')),
        (2, _('Автосалон')),
        (3, _('Поставщик')),
    ]
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.IntegerField(choices=USER_TYPE, default=0, verbose_name=_("Тип пользователя"))
    update_at = models.DateTimeField(auto_now=True, verbose_name=_("Время обновления"))
    email_confirmed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return super().username

    class Meta:
        verbose_name = _("Польлзователь")
        verbose_name_plural = _("Пользователи")
        db_table = "user"
