from django_filters import rest_framework as filters

from apps.car_model.model.models import Car


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CarFilter(filters.FilterSet):
    """
    Фильтр для характеристик автомобиля.
    """

    brand = CharFilterInFilter(field_name='brand', lookup_expr='in')
    weight = filters.RangeFilter()
    engine_capacity = filters.RangeFilter()
    fuel_type = CharFilterInFilter(field_name='fuel_type', lookup_expr='in')
    gearbox_type = CharFilterInFilter(field_name='gearbox_type', lookup_expr='in')
    car_body = CharFilterInFilter(field_name='car_body', lookup_expr='in')

    class Meta:
        model = Car
        fields = ['brand', 'weight', 'engine_capacity', 'fuel_type', 'gearbox_type', 'car_body']
