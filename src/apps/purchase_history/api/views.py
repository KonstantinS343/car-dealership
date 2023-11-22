from rest_framework import viewsets, status, mixins
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from django.db.models import Manager

from .permissions import CarShopPurchasesSalesHistoryСarShowPermission, PurchasesSalesHistorySupplierPermission, BuyerPurchasesSalesHistoryСarShowPermission
from .serializers import PurchasesSalesHistorySupplierSerializer, PurchasesSalesHistoryСarShowSerializer
from apps.purchase_history.models import PurchasesSalesHistorySupplier, PurchasesSalesHistoryСarShow


class PurchasesSalesHistoryСarShowViewSet(viewsets.GenericViewSet):
    """
    ViewSet для работы с историей продаж автосалона.

    Он позволяет только просматривать историю.
    """

    def get_serializer_class(self):
        if self.action == 'carshop_history':
            return PurchasesSalesHistoryСarShowSerializer
        elif self.action == 'buyer_history':
            return PurchasesSalesHistoryСarShowSerializer
        else:
            return super().get_serializer_class()

    @action(methods=["get"], detail=True, permission_classes=[IsAuthenticated, CarShopPurchasesSalesHistoryСarShowPermission])  # type: ignore
    def carshop_history(self, request, pk=None) -> Response:
        """
        Функция возвращает историю продаж автосалона, если у автосалона еще нет продаж,
        то функция возвращает 404 страницу.
        """
        carshow_history = PurchasesSalesHistoryСarShow.objects.filter(car_dealership_id=pk)

        serializer = PurchasesSalesHistoryСarShowSerializer(carshow_history, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "У данного автосалона пустая история"}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=["get"], detail=True, url_path='buyer', permission_classes=[IsAuthenticated, BuyerPurchasesSalesHistoryСarShowPermission])  # type: ignore
    def buyer_history(self, request, pk=None) -> Response:
        """
        Функция возвращает историю покупок клиента, если у клиента еще нет покупок,
        то функция возвращает 404 страницу.
        """
        carshow_history = PurchasesSalesHistoryСarShow.objects.filter(buyer_id=pk)

        serializer = PurchasesSalesHistoryСarShowSerializer(carshow_history, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "У данного клинета пустая история"}, status=status.HTTP_404_NOT_FOUND)


class PurchasesSalesHistorySupplierViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet для работы с историей продаж поставщика.

    Он позволяет только просматривать историю.
    """

    serializer_class = PurchasesSalesHistorySupplierSerializer
    permission_classes = (IsAuthenticated, PurchasesSalesHistorySupplierPermission)

    def get_queryset(self) -> Manager[PurchasesSalesHistorySupplier]:
        return PurchasesSalesHistorySupplier.objects.filter(is_active=True)
