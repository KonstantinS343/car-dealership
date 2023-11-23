from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.db.models import Manager

from typing import List, Any

from .permissions import ActionCarDealershipPermission, ActionSupplierPermission
from .serializers import ActionCarDealershipSerializer, ActionSupplierSerializer
from apps.action.models import ActionCarDealership, ActionSupplier


class ActionCarDealershipViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с акциями автосалона.

    Он предоставляет набор действий для создания, обновления, удаления и просмотра акций.
    """

    serializer_class = ActionCarDealershipSerializer

    def get_permissions(self) -> List[Any]:
        self.permission_classes = (IsAuthenticated,)
        car_show_methods = ('PUT', 'PATCH', 'DELETE', 'POST')
        if self.request.method in car_show_methods:
            self.permission_classes = self.permission_classes + (ActionCarDealershipPermission,)  # type: ignore
        return super(self.__class__, self).get_permissions()

    def get_queryset(self) -> Manager[ActionCarDealership]:
        return ActionCarDealership.objects.filter(is_active=True)


class ActionSupplierViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с акциями поставщика.

    Он предоставляет набор действий для создания, обновления, удаления и просмотра акций.
    """

    serializer_class = ActionSupplierSerializer

    def get_permissions(self) -> List[Any]:
        self.permission_classes = (IsAuthenticated,)
        car_show_methods = ('PUT', 'PATCH', 'DELETE', 'POST')
        if self.request.method in car_show_methods:
            self.permission_classes = self.permission_classes + (ActionSupplierPermission,)  # type: ignore
        return super(self.__class__, self).get_permissions()

    def get_queryset(self) -> Manager[ActionSupplier]:
        return ActionSupplier.objects.filter(is_active=True)
