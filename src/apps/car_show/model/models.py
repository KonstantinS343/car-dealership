from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.common.models import TimeStampedUUIDModel, User
from apps.car_show.model.queryset import CarShowQuerySet
from apps.car_show.model.manager import CarShowManager


class CarShow(TimeStampedUUIDModel):
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

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    name = models.CharField(max_length=255, verbose_name=_("Название"))
    country = CountryField(verbose_name=_("Локация"))
    balance = models.DecimalField(verbose_name=_("Баланс"), default=0.0, max_digits=15, decimal_places=2, validators=[MinValueValidator(0.0)])
    weight = models.FloatField(verbose_name=_("Вес"), validators=[MinValueValidator(0.5), MaxValueValidator(10.0)])
    engine_capacity = models.FloatField(verbose_name=_("Объем двигателя"), validators=[MinValueValidator(1.0), MaxValueValidator(8.0)])
    fuel_type = models.CharField(choices=FUEL_TYPE, verbose_name=_("Тип топлива"))
    gearbox_type = models.CharField(choices=GEARBOX_TYPE, verbose_name=_("Тип коробки передач"))
    car_body = models.CharField(choices=CAR_BODY_TYPE, verbose_name=_("Тип кузова"))

    objects = CarShowManager.from_queryset(CarShowQuerySet)()

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'cars_show'
        verbose_name = _("Автосалон")
        verbose_name_plural = _("Автосалоны")


class CarShowModel(TimeStampedUUIDModel):
    car_dealership = models.ForeignKey(CarShow, on_delete=models.CASCADE, related_name='car_show_model_car_dealership', verbose_name=_("Автосалон"))
    car_model = models.ForeignKey('car_model.Car', on_delete=models.CASCADE, related_name='car_show_model_car', verbose_name=_("Модель автомобиля"))
    model_amount = models.IntegerField(verbose_name=_("Количество автомобилей"), validators=[MinValueValidator(0)], default=1)
    price = models.DecimalField(verbose_name=_("Цена"), validators=[MinValueValidator(0.0)], max_digits=10, decimal_places=2, default=0.0)

    objects = models.Manager.from_queryset(CarShowQuerySet)()

    class Meta:
        db_table = 'cars_show_car_models'
        verbose_name = _("Модель автосалона")
        verbose_name_plural = _("Модели автосалонов")


class UniqueBuyersCarDealership(TimeStampedUUIDModel):
    car_dealership = models.ForeignKey(CarShow, on_delete=models.CASCADE, related_name='unique_buyers_car_show', verbose_name=_("Автосалон"))
    buyer = models.ForeignKey('buyer.Buyer', on_delete=models.CASCADE, related_name='unique_buyers_car_show_buyer', verbose_name=_("Покупатель"))

    objects = models.Manager.from_queryset(CarShowQuerySet)()

    class Meta:
        db_table = 'unique_buyers_car_dealerships'
        verbose_name = _("Уникальный клиент автосалона")
        verbose_name_plural = _("Уникальные клиенты автосалонов")


class CarDealershipSuppliersList(TimeStampedUUIDModel):
    car_dealership = models.ForeignKey(CarShow, on_delete=models.CASCADE, related_name='suppliers_list_car_show', verbose_name=_("Автосалон"))
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.CASCADE, related_name='suppliers_list_supplier', verbose_name=_("Поставщик"))

    objects = models.Manager.from_queryset(CarShowQuerySet)()

    class Meta:
        db_table = 'car_dealerships_suppliers_list'
        verbose_name = _("Поставщик автосалона")
        verbose_name_plural = _("Поставщики автосалонов")
