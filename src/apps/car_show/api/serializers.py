from rest_framework import serializers

from django.shortcuts import get_object_or_404

from apps.car_show.models import CarShow, CarShowModel
from apps.common.models import User
from apps.car_model.api.serilizers import CarModelSerializer


class CarShowSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с автосалонами.

    Этот сериализатор предоставляет функциональность для работы с моделью CarShow.
    В классе есть переопределенный метод create, который привязывает пользователя к созданному автосалону.
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

    def create(self, validated_data):
        user = get_object_or_404(User, id=self.context["request"].user.id)

        return CarShow.objects.create(user=user, **validated_data)


class CarShowModelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с моделями автосалонов.

    Этот сериализатор предоставляет функциональность для работы с моделью CarShowModel.
    """

    car_dealership = CarShowSerializer(read_only=True)
    car_model = CarModelSerializer(read_only=True)

    class Meta:
        model = CarShowModel
        fields = (
            'car_dealership',
            'car_model',
            'model_amount',
        )
