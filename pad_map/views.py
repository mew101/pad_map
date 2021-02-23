from django.urls import path
from django.views import generic
from django.views.generic import TemplateView

class Signup(TemplateView):
    template_name= "signup.html"

class Login(TemplateView):
    template_name= "login.html"

class Dashboard(TemplateView):
    template_name= "dashboard.html"
