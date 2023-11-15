from django.db import models
from django.utils import timezone

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.created_at = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    temperature = models.FloatField()
    time = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['time']

    def __str__(self):
        return f"{self.sensor.name} | {self.temperature}°C | {self.time}"
