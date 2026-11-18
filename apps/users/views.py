from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.

def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse('login')

def logout(request: HttpRequest) -> HttpResponse:
    return HttpResponse('logout')