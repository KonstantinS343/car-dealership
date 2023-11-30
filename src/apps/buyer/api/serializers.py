from rest_framework import serializers

from django.shortcuts import get_object_or_404

from apps.buyer.models import Buyer
from apps.common.models import User
from apps.common.serializers import UserSerializer


class BuyerSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с покупателями.

    Этот сериализатор предоставляет функциональность для работы с моделью Buyer.
    В классе есть переопределенный метод create, который привязывает пользователя к созданному клиенту.
    """

    user = UserSerializer(read_only=True, required=False)

    class Meta:
        model = Buyer
        fields = (
            'user',
            'balance',
        )
        extra_kwargs = {
            "balance": {"read_only": True},
        }

    def create(self, validated_data):
        user = get_object_or_404(User, id=self.context["request"].user.id)

        return Buyer.objects.create(user=user, **validated_data)


class BuyerUpdateSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с покупателями.

    Этот сериализатор предоставляет функциональность для обновление модели Buyer.
    """

    class Meta:
        model = User
        fields = ('first_name', 'last_name')
