from rest_framework import serializers
from .models import Sensor, Measurement

# TODO: опишите необходимые сериализаторы


# class MeasurementSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Measurement
#         fields = ['temperature', 'created_at']


class AddMeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature']


class MeasurementSerializer(serializers.ModelSerializer):
    measurements = AddMeasurementSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ['temperature', 'created_at', 'measurements']



class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
