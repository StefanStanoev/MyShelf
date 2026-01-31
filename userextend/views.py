import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import CreateView
from userextend.forms import SignUpForm



class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = SignUpForm
    success_url = '/login/'


    