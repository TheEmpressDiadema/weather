from django.urls import path

from apps.weather import views

app_name = 'weather'

urlpatterns = [
    path('', views.index, name='index')
]