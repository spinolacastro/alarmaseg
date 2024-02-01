from django.contrib.auth.models import Group, User
from rest_framework import serializers
from alarmavecinal.models import Neighbor, Event



class NeighborSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighbor
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    neighbor = NeighborSerializer()
    class Meta:
        model = User
        fields = ['username', 'email', 'groups', 'neighbor']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'