import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render
from django.views.generic import CreateView
from MyShelf.settings import DEFAULT_FROM_EMAIL
from userextend.forms import SignUpForm
from userextend.models import Logs



class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = SignUpForm
    success_url = '/login/'

    def form_valid(self,form):
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.capitalize()
            new_user.last_name = new_user.last_name.capitalize()
            new_user.save()

            text = f"{new_user.first_name} {new_user.last_name} a fost adaugat cu succes!"
            Logs.objects.create(text=text,created=datetime.datetime.now())

            title = 'Welcome new user'
            content = f"Hello {new_user.first_name} {new_user.last_name}! \n\n Your account has been created successfully! \n\n Please login to continue."

            send_mail(
                subject= title,
                message=content,
                from_email = DEFAULT_FROM_EMAIL,
                recipient_list = [new_user.email]
            )




        return super(UserCreateView, self).form_valid(form)
    
