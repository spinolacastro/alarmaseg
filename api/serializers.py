from django.contrib.auth.models import Group, User
from rest_framework import serializers
from alarmavecinal.models import Profile, Event



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    user_profile = ProfileSerializer()
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'user_profile']
    
    def create(self, validated_data):
        profile_data = validated_data.pop('user_profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'