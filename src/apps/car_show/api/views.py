from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from django.db.models import Manager

from .serializers import CarShowSerializer, CarShowModelSerializer, UniqueBuyersCarDealershipSerializer, CarDealershipSuppliersListSerializer
from .permissions import CarShowPermission
from apps.car_show.model.models import CarShow, CarShowModel, UniqueBuyersCarDealership, CarDealershipSuppliersList
from apps.car_show.statistics import carshow_profit, carshow_sold_cars_amount, carshow_sold_cars_profit
from apps.common.serializers import ProfitSerializer, CarSoldAmountSerializer, CarSoldProfitSerializer


class CarShowViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с автосалонами.

    Этот ViewSet обеспечивает функциональность для работы с автосалонами.
    Он предоставляет набор действий для создания и просмотра, обновления и удаления автосалонов.
    """

    permission_classes = (IsAuthenticated, CarShowPermission)
    serializer_class = CarShowSerializer

    def get_queryset(self) -> Manager[CarShow]:
        if getattr(self, "swagger_fake_view", False):
            # queryset just for schema generation metadata
            return CarShow.objects.none()
        return CarShow.objects.get_carshow_by_user_id(user=self.request.user)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=self.request.user.id)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["get"], detail=True, url_path='cars')
    def car_shop_cars(self, request, pk=None) -> Response:
        """
        Функция возвращает список автомобилей автосалона, если у автосалона еще нет автомобилей,
        то функция возвращает 404 страницу.
        """
        cars = CarShowModel.objects.get_carshow_by_id(id=pk)

        serializer = CarShowModelSerializer(cars, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного автосалона нет автомобилей"}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=["get"], detail=True, url_path='suppliers')
    def carshop_supplier_list(self, request, pk=None) -> Response:
        """
        Функция возвращает список поставщиков автосалона, если у автосалона еще нет поставщиков,
        то функция возвращает 404 страницу.
        """
        suppliers = CarDealershipSuppliersList.objects.get_carshow_by_id(id=pk)

        serializer = CarDealershipSuppliersListSerializer(suppliers, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного автосалона нет поставщиков"}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=["get"], detail=True, url_path='unique')
    def carshop_unique_buyers(self, request, pk=None) -> Response:
        """
        Функция возвращает список уникальных клиентов автосалона, если у автосалона еще нет уникальных клиентов,
        то функция возвращает 404 страницу.
        """
        clients = UniqueBuyersCarDealership.objects.get_carshow_by_id(id=pk)

        serializer = UniqueBuyersCarDealershipSerializer(clients, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного автосалона нет поставщиков"}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=["get"], detail=True, url_path='statistics/profit')
    def carshow_profit(self, request, pk=None) -> Response:
        """
        Функция возвращает общее количество заработанных денег для поставщика.
        """
        profit = carshow_profit(carshow_id=pk)

        serializer = ProfitSerializer(profit)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=True, url_path='statistics/cars/sold')
    def carshow_sold_cars_amount(self, request, pk=None) -> Response:
        """
        Функция возвращает количество проданных автомобилей для поставщика.
        """
        cars_amount = carshow_sold_cars_amount(carshow_id=pk)

        serializer = CarSoldAmountSerializer(cars_amount, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=True, url_path='statistics/cars/sold/profit')
    def carshow_sold_cars_profit(self, request, pk=None) -> Response:
        """
        Функция возвращает количество заработанных денег с каждой модели для поставщика.
        """
        cars_profit = carshow_sold_cars_profit(carshow_id=pk)

        serializer = CarSoldProfitSerializer(cars_profit, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
