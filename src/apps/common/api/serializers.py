from rest_framework import serializers

from djoser.serializers import UserCreateSerializer

from django.utils.translation import gettext_lazy as _

from apps.common.models import User


class UsersSerializer(serializers.ModelSerializer):
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


class CustomUserCreateSerializer(UserCreateSerializer):
    """
    Сериализатор для работы с пользователями.

    Этот сериализатор наследуется от серилизатора создания пользователя
    в библиотеке Djoser и добавляет логику проверки существования почты.
    """

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError(_("Пользователь с такой почтой уже существует."))
        return email
