from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User

# Create your views here.

class LoginView(generic.TemplateView):
    template_name = "login.html"  


class RegisterView(generic.TemplateView):
    template_name = "register.html"  

