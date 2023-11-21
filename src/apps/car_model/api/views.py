from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from apps.car_model.models import CarModel
from .serilizers import CarModelSerializer


class CarViewSet(mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet для работы с авто.

    Этот ViewSet обеспечивает функциональность для работы с автомобилями.
    Он предоставляет функцию просмотра всех автомобилей, а также конкретной модели.
    """

    queryset = CarModel.objects.filter(is_active=True)
    permission_classes = (IsAuthenticated,)
    serializer_class = CarModelSerializer
