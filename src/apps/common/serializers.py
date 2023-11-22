from rest_framework import serializers

from apps.common.models import User


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
