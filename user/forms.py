from django import forms
from django.contrib.auth.forms import UserCreationForm

from user.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
