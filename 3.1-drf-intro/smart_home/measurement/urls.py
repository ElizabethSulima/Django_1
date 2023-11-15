from django.contrib import admin
from django.urls import path
from .views import CreateSensorAPIView, UpdateSensorAPIView, AddMeasurementAPIView, ListSensorsAPIView, RetrieveSensorAPIView


urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('admin/', admin.site.urls),
    path('create/', CreateSensorAPIView.as_view()),
    path('update/', UpdateSensorAPIView.as_view()),
    path('add/', AddMeasurementAPIView.as_view()),
    # path('list/', ListSensorsAPIView.as_view()),
    # path('retrieve/', RetrieveSensorAPIView.as_view()),
]

