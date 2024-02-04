from api import views as apiviews
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken import views
from django.urls import path

schema_view = get_schema_view(title='Alarma Vecinal API')

app_name = 'api'

urlpatterns = [
    path('', schema_view, name='schema'),
    path('token/', views.obtain_auth_token),
    path('pin/', apiviews.PinAdd.as_view(), name='pin-list'),
    path('register/', apiviews.UserAdd.as_view(), name='user-add'),
    path('profile/', apiviews.ProfileRetrieve.as_view(), name='user-list'),
    path('event/', apiviews.EventList.as_view(), name='event-list')
]
