from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=256)
    id = models.CharField(max_length=20)

class Neighborhood(models.Model):
    name = models.CharField(max_length=256)
    police = models.CharField(max_lenth=14)
    fireemergency = models.CharField(max_lenth=14)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    master = models.ForeignKey(User, on_delete=models.CASCADE)
    device = models.CharField(Device, on_delete=models.CASCADE)

class Event(models.Model):
    id = models.PositiveBigIntegerField()
    message = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
