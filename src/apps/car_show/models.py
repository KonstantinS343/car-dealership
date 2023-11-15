from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.utils import timezone

import uuid


class CarShow(models.Model):
    FUEL_TYPE = [
        ('Petrol', _("Бензин")),
        ('Diesel', _("Дизель")),
        ('Electricity', _("Электричество")),
    ]

    GEARBOX_TYPE = [
        ('Mechanical', _("Механическая")),
        ('Automatic', _("Автоматическая")),
    ]

    CAR_BODY_TYPE = [
        ('Sedan', _("Седан")),
        ('Limousine', _("Лимузин")),
        ('Pickup truck', _("Пикап")),
        ('Hatchback', _("Хэтчбек")),
        ('Station wagon', _("Универсал")),
        ('Minivan', _("Минивэн")),
        ('Compartment', _("Купе")),
        ('Convertible', _("Кабриолет")),
    ]

    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    name = models.CharField(max_length=255, verbose_name=_("Название"))
    country = CountryField(verbose_name=_("Локация"))
    balance = models.FloatField(verbose_name=_("Баланс"), default=0.0)
    weight = models.FloatField(verbose_name=_("Вес"))
    engine_capacity = models.FloatField(verbose_name=_("Объем двигателя"))
    fuel_type = models.CharField(choices=FUEL_TYPE, verbose_name=_("Тип топлива"))
    gearbox_type = models.CharField(choices=GEARBOX_TYPE, verbose_name=_("Тип коробки передач"))
    car_body = models.CharField(choices=CAR_BODY_TYPE, verbose_name=_("Тип кузова"))
    creation_time = models.DateTimeField(_("Время создания"), default=timezone.now)
    update_time = models.DateTimeField(_("Время последнего обновления"), default=timezone.now)
    is_active = models.BooleanField(_("Активный"), default=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'car_show'
        verbose_name = _("Автосалон")
        verbose_name_plural = _("Автосалоны")
