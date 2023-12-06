from rest_framework import serializers

from apps.buyer.model.models import Buyer
from apps.common.models import User
from apps.common.api.serializers import UsersSerializer


class BuyerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с покупателями.

    Этот сериализатор предоставляет функциональность для работы с моделью Buyer.
    В классе есть переопределенный метод create, который привязывает пользователя к созданному клиенту.
    """

    user = UsersSerializer(read_only=True, required=False)

    class Meta:
        model = Buyer
        fields = (
            'user',
            'balance',
        )
        extra_kwargs = {
            "balance": {"read_only": True},
        }


class BuyerUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с покупателями.

    Этот сериализатор предоставляет функциональность для обновление модели Buyer.
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
