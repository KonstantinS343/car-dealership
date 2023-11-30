from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.common.models import TimeStampedUUIDModel


class Action(TimeStampedUUIDModel):
    name = models.CharField(max_length=255, verbose_name=_("Название акции"))
    descritpion = models.TextField(verbose_name=_("Описание"))
    event_start = models.DateField(verbose_name=_("Дата начала"))
    event_end = models.DateField(verbose_name=_("Дата окончания"))
    discount = models.DecimalField(verbose_name=_("Скидка"), validators=[MinValueValidator(0.0), MaxValueValidator(1.0)], max_digits=3, decimal_places=2)

    class Meta:
        abstract = True


class ActionCarDealership(Action):
    car_dealership = models.ForeignKey('car_show.CarShow', on_delete=models.CASCADE, related_name='car_show_action', verbose_name=_("Автосалон"))
    car_model = models.ForeignKey('car_model.Car', on_delete=models.CASCADE, related_name='car_show_car_model_action', verbose_name=_("Модель автомобиля"))

    class Meta:
        db_table = 'action_car_dealerships'
        verbose_name = _("Акция автосалона")
        verbose_name_plural = _("Акции автосалонов")


class ActionSupplier(Action):
    supplier = models.ForeignKey('supplier.Supplier', on_delete=models.CASCADE, related_name='supplier_action', verbose_name=_("Поставщик"))
    car_model = models.ForeignKey('car_model.Car', on_delete=models.CASCADE, related_name='supplier_car_model_action', verbose_name=_("Модель автомобиля"))

    class Meta:
        db_table = 'action_suppliers'
        verbose_name = _("Акция поставщика")
        verbose_name_plural = _("Акции поставщиков")
