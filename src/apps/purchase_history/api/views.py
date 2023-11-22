from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from django.db.models import Manager

from .permissions import PurchasesSalesHistoryСarShowPermission, PurchasesSalesHistorySupplierPermission
from .serializers import PurchasesSalesHistorySupplierSerializer, PurchasesSalesHistoryСarShowSerializer
from apps.purchase_history.models import PurchasesSalesHistorySupplier, PurchasesSalesHistoryСarShow


class PurchasesSalesHistoryСarShowViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet для работы с историей продаж автосалона.

    Он позволяет только просматривать историю.
    """

    serializer_class = PurchasesSalesHistoryСarShowSerializer
    permission_classes = (IsAuthenticated, PurchasesSalesHistoryСarShowPermission)

    def get_queryset(self) -> Manager[PurchasesSalesHistoryСarShow]:
        return PurchasesSalesHistoryСarShow.objects.filter(is_active=True)


class PurchasesSalesHistorySupplierViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet для работы с историей продаж поставщика.

    Он позволяет только просматривать историю.
    """

    serializer_class = PurchasesSalesHistorySupplierSerializer
    permission_classes = (IsAuthenticated, PurchasesSalesHistorySupplierPermission)

    def get_queryset(self) -> Manager[PurchasesSalesHistorySupplier]:
        return PurchasesSalesHistorySupplier.objects.filter(is_active=True)
