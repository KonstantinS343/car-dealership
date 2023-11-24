from rest_framework import serializers

from django.shortcuts import get_object_or_404

from apps.supplier.models import Supplier, SupplierCarModel, UniqueBuyersSuppliers
from apps.common.models import User
from apps.car_model.api.serilizers import CarSerializer


class SupplierSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с поставщиками.

    Этот сериализатор предоставляет функциональность для работы с моделью Supplier.
    В классе есть переопределенный метод create, который привязывает пользователя к поставщику.
    """

    class Meta:
        model = Supplier
        fields = (
            'name',
            'country',
            'year_foundation',
            'buyer_amount',
        )
        extra_kwargs = {
            "buyer_amount": {"read_only": True},
        }

    def create(self, validated_data):
        user = get_object_or_404(User, id=self.context["request"].user.id)

        return Supplier.objects.create(user=user, **validated_data)


class SupplierCarModelSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы моделями поставщиков.

    Этот сериализатор предоставляет функциональность для работы с моделью SupplierCarModel.
    """

    supplier = SupplierSerializer(read_only=True)
    car_model = CarSerializer(read_only=True)

    class Meta:
        model = SupplierCarModel
        fields = (
            'supplier',
            'car_model',
            'price',
        )


class UniqueBuyersSuppliersSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы уникальными покупателями поставщиков.

    Этот сериализатор предоставляет функциональность для работы с моделью UniqueBuyersSuppliers.
    """

    from apps.car_show.api.serializers import CarShowSerializer

    supplier = SupplierSerializer(read_only=True)
    car_dealership = CarShowSerializer(read_only=True)

    class Meta:
        model = UniqueBuyersSuppliers
        fields = (
            'supplier',
            'car_dealership',
        )
