from django.contrib.auth.models import Group, User
from rest_framework.response import Response
from rest_framework import generics

from api.serializers import UserSerializer


class ListUsers(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer