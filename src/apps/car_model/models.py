from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.common.models import TimeStampedUUIDModel


class Car(TimeStampedUUIDModel):
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

    brand = models.CharField(max_length=255, verbose_name=_("Марка"))
    weight = models.FloatField(verbose_name=_("Вес"), validators=[MinValueValidator(0.5), MaxValueValidator(10.0)])
    engine_capacity = models.FloatField(verbose_name=_("Объем двигателя"), validators=[MinValueValidator(1.0), MaxValueValidator(8.0)])
    fuel_type = models.CharField(choices=FUEL_TYPE, verbose_name=_("Тип топлива"))
    gearbox_type = models.CharField(choices=GEARBOX_TYPE, verbose_name=_("Тип коробки передач"))
    car_body = models.CharField(choices=CAR_BODY_TYPE, verbose_name=_("Тип кузова"))

    def __str__(self) -> str:
        return self.brand

    class Meta:
        db_table = 'car_models'
        verbose_name = _("Модель автомобиля")
        verbose_name_plural = _("Модели автомобилей")
