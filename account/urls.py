from django import views
from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path("", HomePage.as_view(), name='home'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path("login/", CustomLogin.as_view(), name='login'),
    path('signup/', Register.as_view(), name='signup'),
    path('register/', Registration.as_view(), name='register' )
]
