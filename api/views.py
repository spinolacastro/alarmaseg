from django.contrib.auth.models import Group, User
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from api.serializers import UserSerializer, CreatePinSerializer, EventSerializer, ProfileSerializer
from alarmavecinal.models import Event, Profile
from rest_framework.parsers import JSONParser
from django.http import Http404
import random


class UserAdd(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileRetrieve(APIView):
    permission_class = [IsAuthenticated]

    def get_object(self):
        try:
            return User.objects.get(id=self.request.user.id)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, format=None):
        profile = self.get_object()
        serializer = UserSerializer(profile)
        return Response(serializer.data)

class PinAdd(APIView):
    parser_classes = (JSONParser,)

    def get_object(self, username):
        try:
            obj = User.objects.get(username=username) 
            return obj
        except User.DoesNotExist:
            return False

    def post(self, request, format=None, *args, **kwargs ):
        
        user = self.get_object(self.request.data['username'])
        if not user:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        pwd = random.randint(1,899999) + 100000
        print('seenha', pwd)

        serializer = CreatePinSerializer(user, data={'password': str(pwd)}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response('ok', status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EventList(generics.ListCreateAPIView):
    serializer_class = EventSerializer
    permission_class = [IsAuthenticated]

    def get_queryset(self):
        return Event.objects.all().filter(user__user_profile__neighborhood_id=self.request.user.user_profile.neighborhood_id)

    def list(self, request):
        queryset = self.get_queryset()
        serializer = EventSerializer(queryset, many=True)
        return Response(serializer.data)