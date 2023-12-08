from rest_framework import serializers

from apps.common.models import User
from apps.car_model.api.serilizers import CarSerializer


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с пользователями.

    Этот сериализатор предоставляет функциональность для работы с моделью User.
    """

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'user_type',
            'email_confirmed',
        )
        read_only_fields = fields


class ProfitSerializer(serializers.Serializer):
    """
    Серилизатор для количества заработанных денег.
    """

    total_profit = serializers.FloatField()


class CarSoldAmountSerializer(serializers.Serializer):
    """
    Серилизатор для количества проданных автомобилей.
    """

    car_model = CarSerializer()
    cars_amount = serializers.IntegerField()


class CarSoldProfitSerializer(serializers.Serializer):
    """
    Серилизатор для количества проданных автомобилей.
    """

    car_model = CarSerializer()
    final_model_profit = serializers.FloatField()
