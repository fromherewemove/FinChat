from .views import generate
from django.urls import path

urlpatterns = [
    path("generate/", generate, name="generate")
]
