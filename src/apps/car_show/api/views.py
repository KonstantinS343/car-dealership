from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action

from django.db.utils import IntegrityError
from django.db.models import Manager

from .serializers import CarShowSerializer, CarShowModelSerializer, UniqueBuyersCarDealershipSerializer
from .permissions import CarShowPermission
from apps.car_show.models import CarShow, CarShowModel, UniqueBuyersCarDealership


class CarShowViewSet(
    mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """
    ViewSet для работы с автосалонами.

    Этот ViewSet обеспечивает функциональность для работы с автосалонами.
    Он предоставляет набор действий для создания и просмотра, обновления и удаления автосалонов.
    """

    permission_classes = (IsAuthenticated, CarShowPermission)
    serializer_class = CarShowSerializer

    def get_queryset(self) -> Manager[CarShow]:
        return CarShow.objects.filter(user=self.request.user, is_active=True)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except IntegrityError:
            return Response({"detail": "Один пользователь не может иметь несколько автосалонов"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(methods=["get"], detail=True)  # type: ignore
    def car_shop_cars(self, request, pk=None) -> Response:
        """
        Функция возвращает список автомобилей автосалона, если у автосалона еще нет автомобилей,
        то функция возвращает 404 страницу.
        """
        cars = CarShowModel.objects.filter(car_dealership_id=pk)

        serializer = CarShowModelSerializer(cars, many=True)

        if serializer.data:
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"detail": "У данного автосалона нет автомобилей"}, status=status.HTTP_404_NOT_FOUND)


class UniqueBuyersCarDealershipViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    ViewSet для работы с уникальными клиентами автосалонов.

    Он позволяет только просматривать клиентов автосалона.
    """

    serializer_class = UniqueBuyersCarDealershipSerializer
    permission_classes = (IsAuthenticated, CarShowPermission)

    def get_queryset(self) -> Manager[UniqueBuyersCarDealership]:
        return UniqueBuyersCarDealership.objects.filter(is_active=True)
