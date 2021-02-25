from django.urls import path
from django.views import generic
from django.views.generic import TemplateView
from django.shortcuts import render
from pad_map.forms import InputForm

class Signup(TemplateView):
    template_name= "signup.html"

class Login(TemplateView):
    template_name= "login.html"

class Dashboard(TemplateView):
    template_name= "dashboard.html"

class Profile(TemplateView):
    template_name="profile.html"

def home_view(request):
    context ={}
    context['form']= InputForm()
    return render(request, "profile.html", context)
