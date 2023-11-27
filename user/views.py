from django.shortcuts import render
from django.views.generic import CreateView

from user.forms import RegisterForm
from user.models import User


# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'user/registration.html'


