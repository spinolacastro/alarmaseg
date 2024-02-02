from django.contrib.auth.models import Group, User
from rest_framework.response import Response
from rest_framework import generics, status, viewsets
from rest_framework.views import APIView
from api.serializers import UserSerializer, CreatePinSerializer
from rest_framework.parsers import JSONParser
import random


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PinList(APIView):
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

        