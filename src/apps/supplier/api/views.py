from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from django.db.utils import IntegrityError
from django.db.models import Manager

from .serializers import SupplierSerializer, SupplierCarModelSerializer, UniqueBuyersSuppliersSerializer
from .permissions import SupplierPermission
from apps.supplier.models import Supplier, SupplierCarModel, UniqueBuyersSuppliers


class SupplierViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    ViewSet для работы с поставщиками.

    Этот ViewSet обеспечивает функциональность для работы с поставщиками.
    Он предоставляет набор действий для создания и просмотра, обновления и удаления поставщиков.
    """

    permission_classes = (IsAuthenticated, SupplierPermission)
    serializer_class = SupplierSerializer

    def get_queryset(self) -> Manager[Supplier]:
        return Supplier.objects.filter(user=self.request.user, is_active=True)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except IntegrityError:
            return Response({"detail": "Один пользователь не может являтся несколькими поставщиками"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["get"], detail=True)  # type: ignore
    def supplier_cars(self, request, pk=None) -> Response:
        """
        Функция возвращает список автомобилей поставщика, если у поставщика еще нет автомобилей,
        то функция возвращает 404 страницу.
        """
        cars = SupplierCarModel.objects.filter(supplier_id=pk)

        serializer = SupplierCarModelSerializer(cars, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "У данного поставщика нет автомобилей"}, status=status.HTTP_404_NOT_FOUND)


class UniqueBuyersSuppliersViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet для работы с уникальными клиентами поставщика.

    Он позволяет только просматривать клиентов поставщика.
    """

    serializer_class = UniqueBuyersSuppliersSerializer
    permission_classes = (IsAuthenticated, SupplierPermission)

    def get_queryset(self) -> Manager[UniqueBuyersSuppliers]:
        return UniqueBuyersSuppliers.objects.filter(is_active=True)
