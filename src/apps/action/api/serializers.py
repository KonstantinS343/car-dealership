from rest_framework import serializers

from apps.action.model.models import ActionCarDealership, ActionSupplier
from apps.car_show.model.models import CarShow
from apps.supplier.model.models import Supplier
from apps.car_model.model.models import Car
from apps.car_show.api.serializers import CarShowSerializer
from apps.car_model.api.serilizers import CarSerializer
from apps.supplier.api.serializers import SupplierSerializer


class ActionCarDealershipPostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с акциями автосалона.

    Этот сериализатор предназначен для создание модели ActionCarDealership.
    """

    car_dealership = serializers.PrimaryKeyRelatedField(queryset=CarShow.objects.all())
    car_model = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())

    class Meta:
        model = ActionCarDealership
        fields = (
            'name',
            'car_dealership',
            'car_model',
            'descritpion',
            'event_start',
            'event_end',
            'discount',
        )


class ActionCarDealershipSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с акциями автосалона.

    Этот сериализатор предоставляет функциональность для работы с моделью ActionCarDealership.
    """

    car_dealership = CarShowSerializer(read_only=True)
    car_model = CarSerializer(read_only=True)

    class Meta:
        model = ActionCarDealership
        fields = (
            'name',
            'car_dealership',
            'car_model',
            'descritpion',
            'event_start',
            'event_end',
            'discount',
        )


class ActionSupplierPostSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с акциями поставщика.

    Этот сериализатор предназначен для создание модели ActionSupplier.
    """

    supplier = serializers.PrimaryKeyRelatedField(queryset=Supplier.objects.all())
    car_model = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all())

    class Meta:
        model = ActionSupplier
        fields = (
            'name',
            'supplier',
            'car_model',
            'descritpion',
            'event_start',
            'event_end',
            'discount',
        )


class ActionSupplierSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с акциями поставщика.

    Этот сериализатор предоставляет функциональность для работы с моделью ActionSupplier.
    """

    supplier = SupplierSerializer(read_only=True)
    car_model = CarSerializer(read_only=True)

    class Meta:
        model = ActionSupplier
        fields = (
            'name',
            'supplier',
            'car_model',
            'descritpion',
            'event_start',
            'event_end',
            'discount',
        )
