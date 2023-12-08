from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from django.db.utils import IntegrityError
from django.db.models import Manager

from .serializers import BuyerSerializer, BuyerUpdateSerializer
from .permissions import BuyerPermission
from apps.buyer.model.models import Buyer
from apps.common.statistics import profit, cars_amount, cars_money_sale
from apps.common.serializers import CarSoldAmountSerializer, CarSoldProfitSerializer, ProfitSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с покупателями.

    Этот ViewSet обеспечивает функциональность для работы с покупателями.
    Он предоставляет набор действий для создания и просмотра, обновления и удаления покупателей.
    """

    permission_classes = (IsAuthenticated, BuyerPermission)

    def get_serializer_class(self):
        if self.action == 'update' or self.action == 'partial_update':
            return BuyerUpdateSerializer
        else:
            return BuyerSerializer

    def get_queryset(self) -> Manager[Buyer]:
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return Buyer.objects.none()
        return Buyer.objects.get_buyer_by_user_id(user_id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save(user_id=self.request.user.id)
        except IntegrityError:
            return Response({"detail": "Вы один покупатель!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["get"], detail=True, url_path='statistics/profit')
    def buyer_profit(self, request, pk=None) -> Response:
        """
        Функция возвращает общее количество потраченных денег для покупателя.
        """
        buyer_profit = profit(id=pk, type='buyer')

        serializer = ProfitSerializer(buyer_profit)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=True, url_path='statistics/cars/bought')
    def buyer_sold_cars_amount(self, request, pk=None) -> Response:
        """
        Функция возвращает количество купленных автомобилей для покупателя.
        """
        cars = cars_amount(id=pk, type='buyer')

        serializer = CarSoldAmountSerializer(cars, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=True, url_path='statistics/cars/bought/expenses')
    def buyer_sold_cars_profit(self, request, pk=None) -> Response:
        """
        Функция возвращает количество потраченных денег по каждой модели для покупателя.
        """
        cars_profit = cars_money_sale(id=pk, type='buyer')

        serializer = CarSoldProfitSerializer(cars_profit, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
