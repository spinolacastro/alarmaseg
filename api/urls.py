from api import views
from rest_framework.schemas import get_schema_view
from django.urls import path

schema_view = get_schema_view(title='Alarma Vecinal API')

app_name = 'api'

urlpatterns = [
    path('', schema_view, name='schema'),
    path('users/', views.ListUsers.as_view(), name='user-list'),
]
