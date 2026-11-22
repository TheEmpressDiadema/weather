from django.urls import path

from apps.users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='registration')
]