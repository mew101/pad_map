from django.urls import path
from django.views import generic
from django.views.generic import TemplateView

class Signup(TemplateView):
    template_name= "signup.html"
