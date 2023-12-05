from django_filters import rest_framework as filters

from apps.action.model.models import ActionCarDealership, ActionSupplier


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ActionCarDealershipFilter(filters.FilterSet):
    """
    Фильтр для акций автосалона по автосалону, модели, скидке, начале и конце акции.
    """

    car_dealership = CharFilterInFilter(field_name='car_dealership__name', lookup_expr='in')
    car_model = CharFilterInFilter(field_name='car_model__brand', lookup_expr='in')
    discount = filters.RangeFilter()
    event_start = filters.DateFilter()
    event_end = filters.DateFilter()

    class Meta:
        model = ActionCarDealership
        fields = ['car_dealership', 'car_model', 'discount', 'event_start', 'event_end']


class ActionSupplierFilter(filters.FilterSet):
    """
    Фильтр для акций поставщика по поставщику, модели, скидке, начале и конце акции.
    """

    supplier = CharFilterInFilter(field_name='supplier__name', lookup_expr='in')
    car_model = CharFilterInFilter(field_name='car_model__brand', lookup_expr='in')
    discount = filters.RangeFilter()
    event_start = filters.DateFilter()
    event_end = filters.DateFilter()

    class Meta:
        model = ActionSupplier
        fields = ['supplier', 'car_model', 'discount', 'event_start', 'event_end']
