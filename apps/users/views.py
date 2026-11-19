from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

class UserLoginView(LoginView):

    form_class = AuthenticationForm
    template_name = 'users/login.html'

def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse('logout')