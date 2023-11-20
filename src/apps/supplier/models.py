from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from django.core.validators import MinValueValidator

import datetime
from typing import List, Tuple

from apps.common.models import TimeStampedUUIDModel, User


class Supplier(TimeStampedUUIDModel):
    @staticmethod
    def year_choices() -> List[Tuple[int, int]]:
        return [(year, year) for year in range(1984, datetime.date.today().year + 1)]

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    name = models.CharField(max_length=255, verbose_name=_("Название"))
    country = CountryField(verbose_name=_("Локация"))
    year_foundation = models.IntegerField(_("Год основания"), choices=year_choices())
    buyer_amount = models.IntegerField(verbose_name=_("Количество покупателей"), validators=[MinValueValidator(0)], default=0)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'suppliers'
        verbose_name = _("Поставщик")
        verbose_name_plural = _("Поставщики")


class SupplierCarModel(TimeStampedUUIDModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_car_model', verbose_name=_("Поставщик"))
    car_model = models.ForeignKey(
        'car_model.CarModel', on_delete=models.CASCADE, related_name='car_model_supplier_car_model', verbose_name=_("Модель автомобиля")
    )
    price = models.DecimalField(verbose_name=_("Цена"), validators=[MinValueValidator(0.0)], max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'supplier_cars'
        verbose_name = _("Автомобиль поставщика")
        verbose_name_plural = _("Автомобили поставщиков")


class UniqueBuyersSuppliers(TimeStampedUUIDModel):
    car_dealership = models.ForeignKey(
        'car_show.CarShow', on_delete=models.CASCADE, related_name='unique_buyers_supplier_car_show', verbose_name=_("Автосалон")
    )
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='unique_buyers_supplier', verbose_name=_("Поставщик"))

    class Meta:
        db_table = 'unique_buyers_suppliers'
        verbose_name = _("Уникальный клиент поставщика")
        verbose_name_plural = _("Уникальные клиенты поставщиков")
