from django.shortcuts import render
from . import forms
from django.views.generic import CreateView
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
# Create your views here.

class SignUp(CreateView):
        form_class = forms.UserCreateForm
        success_url = reverse_lazy("home")
        template_name = "accounts/signup.html"

class CustomPasswordResetView(PasswordResetView):
    #template_name = 'accounts/password_reset.html'
        pass