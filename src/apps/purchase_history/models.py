from django.db import models
from django.utils.translation import gettext_lazy as _

import uuid

from apps.common.models import TimeStampedUUIDModel


class PurchasesSalesHistorySupplier(TimeStampedUUIDModel):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    supplier = models.ForeignKey('Supplier',
                                 on_delete=models.CASCADE,
                                 related_name='purchases_history_supplier',
                                 verbose_name=_("Поставщик"))
    car_dealership = models.ForeignKey('CarShow',
                                       on_delete=models.CASCADE,
                                       related_name='purchases_history_supplier_car_show',
                                       verbose_name=_("Автосалон"))
    car_model = models.ForeignKey('CarModel',
                                  on_delete=models.CASCADE,
                                  related_name='purchases_history_supplier_car_model',
                                  verbose_name=_("Модель автомобиля"))
    final_price = models.FloatField(verbose_name=_("Итоговая цена"))

    class Meta:
        db_table = 'purchases_history_suppliers'
        verbose_name = _("Продажа поставщика")
        verbose_name_plural = _("Продажи поставщиков")


class PurchasesSalesHistoryСarShow(TimeStampedUUIDModel):
    id = models.UUIDField(
         primary_key=True,
         default=uuid.uuid4,
         editable=False)
    buyer = models.ForeignKey('Buyer',
                              on_delete=models.CASCADE,
                              related_name='purchases_history_car_show_buyer',
                              verbose_name=_("Покупатель"))
    car_dealership = models.ForeignKey('CarShow',
                                       on_delete=models.CASCADE,
                                       related_name='purchases_history_car_show',
                                       verbose_name=_("Автосалон"))
    car_model = models.ForeignKey('CarModel',
                                  on_delete=models.CASCADE,
                                  related_name='purchases_history_car_show_car_model',
                                  verbose_name=_("Модель автомобиля"))
    final_price = models.FloatField(verbose_name=_("Итоговая цена"))

    class Meta:
        db_table = 'purchases_history_car_shows'
        verbose_name = _("Продажа автосалона")
        verbose_name_plural = _("Продажи автосалонов")
