from django.contrib.auth import login
from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, TemplateView
from user.forms import RegisterForm, LoginForm
from user.models import User


# Create your views here.

class RegisterView(CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'user/registration.html'
    success_url = reverse_lazy('login')


class LoginView(TemplateView):
    template_name = 'user/login.html'

    def post(self, request: HttpRequest):
        if request == 'POST':
            login_form = LoginForm(request.POST)
            if login_form.is_valid():
                user_email = login_form.cleaned_data.get('email')
                user_password = login_form.cleaned_data.get('password')
                user: User = User.objects.filter(email__iexact=user_email).first()
                password_check = user.check_password(user_password)
                if password_check:
                    login(request.user)
                    return redirect(reverse('todo_list'))
        else:
            login_form = LoginForm()
            context = {'login_form': login_form}
            return render(request, 'user/login.html', context)