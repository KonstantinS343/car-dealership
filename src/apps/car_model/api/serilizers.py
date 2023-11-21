from rest_framework import serializers


from apps.car_model.models import CarModel


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = (
            'brand',
            'weight',
            'engine_capacity',
            'fuel_type',
            'gearbox_type',
            'car_body',
        )
