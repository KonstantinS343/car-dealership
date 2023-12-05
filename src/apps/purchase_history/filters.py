from django_filters import rest_framework as filters

from apps.purchase_history.model.models import PurchasesSalesHistorySupplier, PurchasesSalesHistoryСarShow


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class PurchasesSalesHistoryСarShowFilter(filters.FilterSet):
    """
    Фильтр для цены и марки автомобиля в истории покупок для автосалонов и покупателей.
    """

    final_price = filters.RangeFilter()
    car_model = CharFilterInFilter(field_name='car_model__brand', lookup_expr='in')

    class Meta:
        model = PurchasesSalesHistoryСarShow
        fields = ['final_price', 'car_model']


class PurchasesSalesHistorySupplierFilter(filters.FilterSet):
    """
    Фильтр для цены и марки автомобиля в истории продаж для поставщиков.
    """

    final_price = filters.RangeFilter()
    car_model = CharFilterInFilter(field_name='car_model__brand', lookup_expr='in')

    class Meta:
        model = PurchasesSalesHistorySupplier
        fields = ['final_price', 'car_model']
