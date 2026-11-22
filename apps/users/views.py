from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView

from apps.users.forms import UserLoginForm, UserRegisterForm
# Create your views here.

class LoginUser(LoginView):

    form_class = UserLoginForm
    template_name = 'users/login.html'
    extra_context = {'title' : 'Authorization'}

class RegisterView(CreateView):

    form_class = UserRegisterForm
    template_name = 'users/register.html'
    extra_context = {'title' : 'Registration'}
    success_url = reverse_lazy('home')