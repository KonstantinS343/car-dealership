from rest_framework import serializers

from apps.car_show.api.serializers import CarShowSerializer
from apps.car_model.api.serilizers import CarModelSerializer
from apps.supplier.api.serializers import SupplierSerializer
from apps.buyer.api.serializers import BuyerSerializer
from apps.purchase_history.models import PurchasesSalesHistoryСarShow, PurchasesSalesHistorySupplier


class PurchasesSalesHistoryСarShowSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с историей продаж автосалонов.

    Этот сериализатор предоставляет функциональность для работы с моделью PurchasesSalesHistoryСarShow.
    """

    car_dealership = CarShowSerializer(read_only=True)
    car_model = CarModelSerializer(read_only=True)
    buyer = BuyerSerializer(read_only=True)

    class Meta:
        model = PurchasesSalesHistoryСarShow
        fields = (
            'buyer',
            'car_dealership',
            'car_model',
            'final_price',
        )
        read_only_fields = fields


class PurchasesSalesHistorySupplierSerializer(serializers.ModelSerializer):
    """
    Сериализатор для работы с историей продаж поставщиков.

    Этот сериализатор предоставляет функциональность для работы с моделью PurchasesSalesHistorySupplier.
    """

    car_dealership = CarShowSerializer(read_only=True)
    car_model = CarModelSerializer(read_only=True)
    supplier = SupplierSerializer(read_only=True)

    class Meta:
        model = PurchasesSalesHistorySupplier
        fields = (
            'supplier',
            'car_dealership',
            'car_model',
            'final_price',
        )
        read_only_fields = fields
