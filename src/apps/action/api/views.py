from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django.db.models import Manager

from typing import List, Any

from .permissions import ActionCarDealershipPermission, ActionSupplierPermission
from .serializers import ActionCarDealershipSerializer, ActionSupplierSerializer, ActionCarDealershipPostSerializer, ActionSupplierPostSerializer
from apps.action.model.models import ActionCarDealership, ActionSupplier


class ActionCarDealershipViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с акциями автосалона.

    Он предоставляет набор действий для создания, обновления, удаления и просмотра акций.
    """

    def get_serializer_class(self):
        if self.action == 'create':
            return ActionCarDealershipPostSerializer
        else:
            return ActionCarDealershipSerializer

    def get_permissions(self) -> List[Any]:
        self.permission_classes = (IsAuthenticated,)
        car_show_methods = ('PUT', 'PATCH', 'DELETE', 'POST')
        if self.request.method in car_show_methods:
            self.permission_classes = self.permission_classes + (ActionCarDealershipPermission,)  # type: ignore
        return super(self.__class__, self).get_permissions()

    def get_queryset(self) -> Manager[ActionCarDealership]:
        return ActionCarDealership.objects.for_action()


class ActionSupplierViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с акциями поставщика.

    Он предоставляет набор действий для создания, обновления, удаления и просмотра акций.
    """

    def get_serializer_class(self):
        if self.action == 'create':
            return ActionSupplierPostSerializer
        else:
            return ActionSupplierSerializer

    def get_permissions(self) -> List[Any]:
        self.permission_classes = (IsAuthenticated,)
        car_show_methods = ('PUT', 'PATCH', 'DELETE', 'POST')
        if self.request.method in car_show_methods:
            self.permission_classes = self.permission_classes + (ActionSupplierPermission,)  # type: ignore
        return super(self.__class__, self).get_permissions()

    def get_queryset(self) -> Manager[ActionSupplier]:
        return ActionSupplier.objects.for_action()
