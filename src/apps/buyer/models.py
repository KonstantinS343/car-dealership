from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator


from apps.common.models import User, TimeStampedUUIDModel


class Buyer(TimeStampedUUIDModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("Пользователь"))
    balance = models.DecimalField(verbose_name=_("Баланс"),
                                  default=0.0,
                                  max_digits=15,
                                  decimal_places=2,
                                  validators=[MinValueValidator(0.0)])

    def __str__(self) -> str:
        return self.user.username

    class Meta:
        verbose_name = _("Покупатель")
        verbose_name_plural = _("Покупатели")
        db_table = 'buyer'
