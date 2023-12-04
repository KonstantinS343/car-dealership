from django.db import models


class PurchasesSalesHistoryQuerySet(models.QuerySet):
    """
    QuerySet, который возвращает историю покупок/продаж для конкретного пользователя.
    """

    def car_show_history(self, id) -> models.Manager[models.Model]:
        return self.filter(car_dealership_id=id, is_active=True)

    def buyer_history(self, id) -> models.Manager[models.Model]:
        return self.filter(buyer_id=id, is_active=True)

    def supplier_history(self, id) -> models.Manager[models.Model]:
        return self.filter(supplier_id=id, is_active=True)
