from django.contrib.auth.models import Group, User
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from api.serializers import UserSerializer


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer