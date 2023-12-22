from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from django.db.models import Manager
from django_filters import rest_framework as filters


from .permissions import CarShopPurchasesSalesHistoryСarShowPermission, PurchasesSalesHistorySupplierPermission, BuyerPurchasesSalesHistoryСarShowPermission
from .serializers import PurchasesSalesHistorySupplierSerializer, PurchasesSalesHistoryСarShowSerializer
from apps.purchase_history.model.models import PurchasesSalesHistorySupplier, PurchasesSalesHistoryСarShow
from apps.purchase_history.filters import PurchasesSalesHistoryСarShowFilter, PurchasesSalesHistorySupplierFilter


class PurchasesSalesHistoryСarShowViewSet(viewsets.GenericViewSet):
    """
    ViewSet для работы с историей продаж автосалона.

    Он позволяет только просматривать историю.
    """

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PurchasesSalesHistoryСarShowFilter

    def get_serializer_class(self):
        if self.action == 'carshop_history':
            return PurchasesSalesHistoryСarShowSerializer
        elif self.action == 'buyer_history':
            return PurchasesSalesHistoryСarShowSerializer
        else:
            return super().get_serializer_class()

    def get_queryset(self) -> Manager[PurchasesSalesHistoryСarShow]:
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return PurchasesSalesHistoryСarShow.objects.none()
        pk = self.kwargs['pk']
        if self.action == 'carshop_history':
            return PurchasesSalesHistoryСarShow.objects.car_show_history(id=pk)
        elif self.action == 'buyer_history':
            return PurchasesSalesHistoryСarShow.objects.buyer_history(id=pk)

    @action(methods=["get"], detail=True, url_path='history', permission_classes=[IsAuthenticated, CarShopPurchasesSalesHistoryСarShowPermission])
    def carshop_history(self, request, pk=None) -> Response:
        """
        Функция возвращает историю продаж автосалона, если у автосалона еще нет продаж,
        то функция возвращает 404 страницу.
        """
        carshow_history = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(carshow_history, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного автосалона пустая история"}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=["get"], detail=True, url_path='buyer/history', permission_classes=[IsAuthenticated, BuyerPurchasesSalesHistoryСarShowPermission])
    def buyer_history(self, request, pk=None) -> Response:
        """
        Функция возвращает историю покупок клиента, если у клиента еще нет покупок,
        то функция возвращает 404 страницу.
        """
        carshow_history = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(carshow_history, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного клинета пустая история"}, status=status.HTTP_404_NOT_FOUND)


class PurchasesSalesHistorySupplierViewSet(viewsets.GenericViewSet):
    """
    ViewSet для работы с историей продаж поставщика.

    Он позволяет только просматривать историю.
    """

    serializer_class = PurchasesSalesHistorySupplierSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PurchasesSalesHistorySupplierFilter

    def get_queryset(self) -> Manager[PurchasesSalesHistorySupplier]:
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return PurchasesSalesHistorySupplier.objects.none()
        pk = self.kwargs['pk']
        return PurchasesSalesHistorySupplier.objects.supplier_history(id=pk)

    @action(methods=["get"], detail=True, url_path='history', permission_classes=[IsAuthenticated, PurchasesSalesHistorySupplierPermission])
    def supplier_history(self, request, pk=None) -> Response:
        """
        Функция возвращает историю продаж поставщика, если у поставщика еще нет покупок,
        то функция возвращает 404 страницу.
        """
        supplier_history = self.filter_queryset(self.get_queryset())

        serializer = self.get_serializer(supplier_history, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного поставщика пустая история"}, status=status.HTTP_404_NOT_FOUND)
