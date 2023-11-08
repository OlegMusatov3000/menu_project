from .views import Home
from django.urls import path

urlpatterns = [
    path('', Home, name='home'),
    path('contacts/', Home, name='Contacts'),
    path('<str:URL_Name>/', Home, name='home'),
]
