from rest_framework import serializers


from apps.car_model.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = (
            'brand',
            'weight',
            'engine_capacity',
            'fuel_type',
            'gearbox_type',
            'car_body',
        )
