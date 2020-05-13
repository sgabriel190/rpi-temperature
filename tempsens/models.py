from django.db import models

# Create your models here.
class Temperature(models.Model):
    temperature_value = models.IntegerField(default=0)
    humidity_value =  models.IntegerField(default=0)
    time_value = models.CharField(max_length=25)
