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

    def get_sales_profit(self, id, type='supplier') -> models.Manager[models.Model]:
        queryset = self.filter(supplier_id=id, is_active=True) if type == 'supplier' else self.filter(car_dealership=id, is_active=True)
        return queryset.aggregate(total_profit=models.Sum('final_price'))

    def get_sold_cars_amount(self, id, type='supplier') -> models.Manager[models.Model]:
        queryset = self.filter(supplier_id=id, is_active=True) if type == 'supplier' else self.filter(car_dealership=id, is_active=True)
        return queryset.select_related('car_model').annotate(cars_amount=models.Count('car_model'))

    def get_sold_cars_profit(self, id, type='supplier') -> models.Manager[models.Model]:
        queryset = self.filter(supplier_id=id, is_active=True) if type == 'supplier' else self.filter(car_dealership=id, is_active=True)
        return queryset.annotate(final_model_profit=models.Sum('final_price'))
