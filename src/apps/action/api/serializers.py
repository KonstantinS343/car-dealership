from rest_framework import serializers

from apps.action.models import ActionCarDealership


class ActionCarDealershipSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с акциями автомобильного дилера.

    Этот сериализатор предоставляет функциональность для работы с моделью ActionCarDealership.
    """

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
