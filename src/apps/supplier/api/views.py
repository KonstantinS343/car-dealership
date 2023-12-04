from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from django.db.utils import IntegrityError
from django.db.models import Manager

from .serializers import SupplierSerializer, SupplierCarModelSerializer, UniqueBuyersSuppliersSerializer
from .permissions import SupplierPermission
from apps.supplier.model.models import Supplier, SupplierCarModel, UniqueBuyersSuppliers


class SupplierViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с поставщиками.

    Этот ViewSet обеспечивает функциональность для работы с поставщиками.
    Он предоставляет набор действий для создания и просмотра, обновления и удаления поставщиков.
    """

    permission_classes = (IsAuthenticated, SupplierPermission)
    serializer_class = SupplierSerializer

    def get_queryset(self) -> Manager[Supplier]:
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Supplier.objects.none()
        return Supplier.objects.get_supplier_by_user_id(user=self.request.user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(user_id=self.request.user.id)
        except IntegrityError:
            return Response({"detail": "Один пользователь не может являтся несколькими поставщиками"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["get"], detail=True, url_path='cars')
    def supplier_cars(self, request, pk=None) -> Response:
        """
        Функция возвращает список автомобилей поставщика, если у поставщика еще нет автомобилей,
        то функция возвращает 404 страницу.
        """
        cars = SupplierCarModel.objects.get_supplier_by_id(supplier=pk)

        serializer = SupplierCarModelSerializer(cars, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного поставщика нет автомобилей"}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=["get"], detail=True, url_path='unique')
    def supplier_unique_buyers(self, request, pk=None) -> Response:
        """
        Функция возвращает список уникальных клиентов поставщика, если у автосалона еще нет уникальных поставщика,
        то функция возвращает 404 страницу.
        """
        clients = UniqueBuyersSuppliers.objects.get_supplier_by_id(supplier=pk)

        serializer = UniqueBuyersSuppliersSerializer(clients, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного поставщика нет уникальных клиентов"}, status=status.HTTP_404_NOT_FOUND)
