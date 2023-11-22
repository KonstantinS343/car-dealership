from rest_framework import serializers

from apps.action.models import ActionCarDealership, ActionSupplier
from apps.car_show.api.serializers import CarShowSerializer
from apps.car_model.api.serilizers import CarModelSerializer
from apps.supplier.api.serializers import SupplierSerializer


class ActionCarDealershipSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с акциями автомобильного дилера.

    Этот сериализатор предоставляет функциональность для работы с моделью ActionCarDealership.
    """

    car_dealership = CarShowSerializer(read_only=True)
    car_model = CarModelSerializer(read_only=True)

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


class ActionSupplierSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с акциями поставщика.

    Этот сериализатор предоставляет функциональность для работы с моделью ActionSupplier.
    """

    supplier = SupplierSerializer(read_only=True)
    car_model = CarModelSerializer(read_only=True)

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
