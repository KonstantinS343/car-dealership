from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django_filters import rest_framework as filters

from apps.car_model.model.models import Car
from .serilizers import CarSerializer
from apps.car_model.filters import CarFilter


class CarViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet для работы с авто.

    Этот ViewSet обеспечивает функциональность для работы с автомобилями.
    Он предоставляет функцию просмотра всех автомобилей, а также конкретной модели.
    """

    queryset = Car.objects.cars()
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = CarFilter
