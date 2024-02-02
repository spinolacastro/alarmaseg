from django.db import models
from django.contrib.auth.models import User, Group

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=2)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.short_name

class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=256)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=256)
    serial = models.CharField(max_length=20)
    brand = models.CharField(max_length=40)

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

class Profile(models.Model):
    user = models.OneToOneField(User, related_name="user_profile", on_delete=models.CASCADE, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=256)
    address2 = models.CharField(max_length=256)
    street_number = models.CharField(max_length=256)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Event(models.Model):
    id = models.BigAutoField(primary_key=True)
    message = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return 'Event: {}'.format(self.id)
