from django.db import models


class PurchasesSalesHistoryQuerySet(models.QuerySet):
    """
    QuerySet, который возвращает историю покупок/продаж для конкретного пользователя.
    """

    def car_show_history(self, id) -> models.Manager[models.Model]:
        return self.filter(car_dealership_id=id, is_active=True).select_related('car_dealership', 'car_model', 'buyer', 'buyer__user')

    def buyer_history(self, id) -> models.Manager[models.Model]:
        return self.filter(buyer_id=id, is_active=True).select_related('car_dealership', 'car_model', 'buyer')

    def supplier_history(self, id) -> models.Manager[models.Model]:
        return self.filter(supplier_id=id, is_active=True).select_related('car_dealership', 'car_model', 'supplier')

    def get_sales(self, queryset) -> models.Manager[models.Model]:
        return queryset.aggregate(total_profit=models.Sum('final_price'))

    def get_cars_amount(self, queryset) -> models.Manager[models.Model]:
        return queryset.select_related('car_model').annotate(cars_amount=models.Count('car_model'))

    def get_cars(self, queryset) -> models.Manager[models.Model]:
        return queryset.annotate(final_model_profit=models.Sum('final_price'))

    def get_popular_car_brand(self) -> models.Manager[models.Manager]:
        return self.values('car_model__brand').annotate(count_car=models.Count('car_dealership_id')).order_by('-count_car')
