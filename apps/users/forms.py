from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm


class UserLoginForm(AuthenticationForm):

    username = forms.CharField(
        label='Login', 
        widget=forms.TextInput(attrs={'class' : 'form-input'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class' : 'form-input'})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class UserRegisterForm(UserCreationForm):

    username = forms.CharField(
        label='Login',
        max_length=50
    )
    password1 = forms.CharField(
        label='Password',
        max_length=30,
        widget=forms.PasswordInput(attrs={'class' : 'form-input'})
    )
    password2 = forms.CharField(
        label='Confirm password',
        max_length=30,
        widget=forms.PasswordInput(attrs={'class' : 'form-input'})
    )

    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']