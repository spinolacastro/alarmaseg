from django.contrib.auth.models import Group, User
from rest_framework import serializers
from alarmavecinal.models import *

class DeviceSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = '__all__'


class NeighborhoodSerializer(serializers.ModelSerializer):
    device = DeviceSerialzier()
    admin = serializers.SlugRelatedField(
        read_only=True,
        slug_field='email'
    )
    master = serializers.SlugRelatedField(
        read_only=True,
        slug_field='email'
    )

    class Meta:
        model = Neighborhood
        fields = '__all__'


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


class CreatePinSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return instance


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']


class ProfileDetailSerializer(serializers.ModelSerializer):
    user = UserDetailSerializer()
    neighborhood = NeighborhoodSerializer()
    country = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    state = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    city = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = Profile
        fields = '__all__'