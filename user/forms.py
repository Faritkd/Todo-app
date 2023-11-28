from django import forms
from user.models import User


class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password']


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)