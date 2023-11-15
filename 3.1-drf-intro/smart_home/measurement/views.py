# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from .models import Sensor, Measurement
from .serializers import MeasurementSerializer, SensorDetailSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response


# Create a new sensor
class CreateSensorAPIView(ListAPIView):
    serializer_class = SensorDetailSerializer

    def post(self, request, *args, **kwargs):
        sensor_data = request.data
        try:
            sensor = Sensor.objects.get(name=sensor_data['name'])
            return Response({'message': 'Sensor already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Sensor.DoesNotExist:
            new_sensor = Sensor.objects.create(**sensor_data)
            serializer = SensorDetailSerializer(new_sensor)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


# Update an existing sensor
class UpdateSensorAPIView(ListAPIView):
    serializer_class = SensorDetailSerializer

    def put(self, request, pk, *args, **kwargs):
        try:
            sensor_pk = get_object_or_404(Sensor, pk=pk)
            sensor_data = request.data.get('sensor')
            sensor_obj = Sensor.objects.filter(pk=sensor_pk).update(**sensor_data)

            if not sensor_obj:
                return Response({"error": "Sensor doesn't exist"}, status=status.HTTP_404_NOT_FOUND)

            return Response({}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"Internal Server Error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Add a new measurement to a sensor
class AddMeasurementAPIView(ListAPIView):
    serializer_class = MeasurementSerializer

    def post(self, request, sensor_pk, *args, **kwargs):
        measurement_data = request.data.get('measurement')
        try:
            sensor = get_object_or_404(Sensor, id=sensor_pk)
        except Sensor.DoesNotExist:
            return Response({"Error": "Invalid sensor"}, status=status.HTTP_400_BAD_REQUEST)
        if measurement_data:
            measurement = Measurement.objects.create(sensor=sensor, **measurement_data)
            serializer = MeasurementSerializer(measurement)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# List all sensors
class ListSensorsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        sensors = Sensor.objects.all()
        serializer = SensorDetailSerializer(sensors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Get a specific sensor
class RetrieveSensorAPIView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            sensor = get_object_or_404(Sensor, id=pk)
            serializer = SensorDetailSerializer(sensor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Sensor.DoesNotExist:
            return Response({"Sensor.DoesNotExist": str(pk)}, status=status.HTTP_404_NOT_FOUND)

