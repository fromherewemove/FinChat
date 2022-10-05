import email
from django.views.generic.list import * 
from django.views.generic import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from account.models import CustomUser
from django.contrib.auth.views import LoginView, LogoutView
# Create your views here.
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .form import *


class CustomLogin(LoginView):
    template_name = 'account/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')

class Registration(CreateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'date_of_birth', 'bvn', 'email']
    success_url = reverse_lazy('home')
    template_name = 'account/register.html'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Registration, self).form_valid(form)
    
class Register(FormView):
    form_class = SignupForm
    template_name = 'account/signup.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register,self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(Register, self).get(*args, **kwargs)

class HomePage(LoginRequiredMixin, ListView):
    model = CustomUser
    context_object_name = 'home'
    template_name = 'account/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['home'] = context['home'].filter(user=self.request.user)
        return context