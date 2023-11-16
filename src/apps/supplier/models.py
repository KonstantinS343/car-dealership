from django.db import models
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField

import datetime

from apps.common.models import TimeStampedUUIDModel


class Supplier(TimeStampedUUIDModel):

    def year_choices():
        return [(year, year) for year in range(1984, datetime.date.today().year+1)]

    name = models.CharField(max_length=255, verbose_name=_("Название"))
    country = CountryField(verbose_name=_("Локация"))
    year_foundation = models.IntegerField(_("Год основания"), choices=year_choices())
    buyer_amount = models.IntegerField(verbose_name=_("Количество покупателей"))

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'suppliers'
        verbose_name = _("Поставщик")
        verbose_name_plural = _("Поставщики")


class SupplierCarModel(TimeStampedUUIDModel):
    supplier = models.ForeignKey(Supplier,
                                 on_delete=models.CASCADE,
                                 related_name='supplier_car_model',
                                 verbose_name=_("Поставщик"))
    car_model = models.ForeignKey('car_model.CarModel',
                                  on_delete=models.CASCADE,
                                  related_name='car_model_supplier_car_model',
                                  verbose_name=_("Модель автомобиля"))
    price = models.FloatField(verbose_name=_("Цена"))

    class Meta:
        db_table = 'supplier_cars'
        verbose_name = _("Автомобиль поставщика")
        verbose_name_plural = _("Автомобили поставщиков")


class UniqueBuyersSuppliers(TimeStampedUUIDModel):
    car_dealership = models.ForeignKey('car_show.CarShow',
                                       on_delete=models.CASCADE,
                                       related_name='unique_buyers_supplier_car_show',
                                       verbose_name=_("Автосалон"))
    supplier = models.ForeignKey(Supplier,
                                 on_delete=models.CASCADE,
                                 related_name='unique_buyers_supplier',
                                 verbose_name=_("Поставщик"))

    class Meta:
        db_table = 'unique_buyers_suppliers'
        verbose_name = _("Уникальный клиент поставщика")
        verbose_name_plural = _("Уникальные клиенты поставщиков")