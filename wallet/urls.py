from django.urls import path
from .views import create_wallet

urlpatterns = [
    path('', create_wallet, name='wallet')
]
