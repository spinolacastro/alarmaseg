from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Device(models.Model):
    name = models.CharField(max_length=256)
    serial = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Neighborhood(models.Model):
    name = models.CharField(max_length=256)
    police = models.CharField(max_length=14)
    fireemergency = models.CharField(max_length=14)
    admin = models.ForeignKey(User, related_name="admin", on_delete=models.CASCADE, null=True)
    master = models.ForeignKey(User, related_name="master", on_delete=models.CASCADE, null=True)
    device = models.OneToOneField(Device, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

class Neighbor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)

class Event(models.Model):
    id = models.PositiveBigIntegerField(primary_key=True)
    message = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return 'Event: {}'.format(self.id)

