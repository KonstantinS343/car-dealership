from rest_framework import serializers

from django.shortcuts import get_object_or_404

from apps.car_show.models import CarShow, CarShowModel, UniqueBuyersCarDealership, CarDealershipSuppliersList
from apps.common.models import User
from apps.car_model.api.serilizers import CarSerializer
from apps.buyer.api.serializers import BuyerSerializer


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
    car_model = CarSerializer(read_only=True)

    class Meta:
        model = CarShowModel
        fields = (
            'car_dealership',
            'car_model',
            'model_amount',
        )


class UniqueBuyersCarDealershipSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы уникальными покупателями автосалонов.

    Этот сериализатор предоставляет функциональность для работы с моделью UniqueBuyersCarDealership.
    """

    buyer = BuyerSerializer(read_only=True)
    car_dealership = CarShowSerializer(read_only=True)

    class Meta:
        model = UniqueBuyersCarDealership
        fields = (
            'buyer',
            'car_dealership',
        )


class CarDealershipSuppliersListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с списком поставщиков автосалонов.

    Этот сериализатор предоставляет функциональность для работы с моделью CarDealershipSuppliersList.
    """

    from apps.supplier.api.serializers import SupplierSerializer

    supplier = SupplierSerializer(read_only=True)
    car_dealership = CarShowSerializer(read_only=True)

    class Meta:
        model = CarDealershipSuppliersList
        fields = (
            'supplier',
            'car_dealership',
        )
