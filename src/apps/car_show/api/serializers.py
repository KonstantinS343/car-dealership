from rest_framework import serializers

from apps.car_show.models import CarShow


class CarShowSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы автосалонами.

    Этот сериализатор предоставляет функциональность для работы с моделью CarShow.
    """

    class Meta:
        model = CarShow
        fields = (
            'name',
            'country',
            'balance',
            'weight',
            'engine_capacity',
            'fuel_type',
            'gearbox_type',
            'car_body',
        )
        extra_kwargs = {
            "balance": {"read_only": True},
        }
