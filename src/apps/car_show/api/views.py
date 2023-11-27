from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from django.db.models import Manager

from .serializers import CarShowSerializer, CarShowModelSerializer, UniqueBuyersCarDealershipSerializer, CarDealershipSuppliersListSerializer
from .permissions import CarShowPermission
from apps.car_show.models import CarShow, CarShowModel, UniqueBuyersCarDealership, CarDealershipSuppliersList


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
        return CarShow.objects.filter(user=self.request.user, is_active=True)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["get"], detail=True, url_path='cars')  # type: ignore
    def car_shop_cars(self, request, pk=None) -> Response:
        """
        Функция возвращает список автомобилей автосалона, если у автосалона еще нет автомобилей,
        то функция возвращает 404 страницу.
        """
        cars = CarShowModel.objects.filter(car_dealership_id=pk)

        serializer = CarShowModelSerializer(cars, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного автосалона нет автомобилей"}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=["get"], detail=True, url_path='suppliers')  # type: ignore
    def carshop_supplier_list(self, request, pk=None) -> Response:
        """
        Функция возвращает список поставщиков автосалона, если у автосалона еще нет поставщиков,
        то функция возвращает 404 страницу.
        """
        suppliers = CarDealershipSuppliersList.objects.filter(car_dealership_id=pk)

        serializer = CarDealershipSuppliersListSerializer(suppliers, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного автосалона нет поставщиков"}, status=status.HTTP_404_NOT_FOUND)

    @action(methods=["get"], detail=True, url_path='unique')  # type: ignore
    def carshop_unique_buyers(self, request, pk=None) -> Response:
        """
        Функция возвращает список уникальных клиентов автосалона, если у автосалона еще нет уникальных клиентов,
        то функция возвращает 404 страницу.
        """
        clients = UniqueBuyersCarDealership.objects.filter(car_dealership_id=pk)

        serializer = UniqueBuyersCarDealershipSerializer(clients, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"detail": "У данного автосалона нет поставщиков"}, status=status.HTTP_404_NOT_FOUND)
