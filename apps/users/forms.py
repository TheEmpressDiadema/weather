from django import forms


class UserLoginForm(forms.Form):

    username = forms.CharField(
        label='Login', 
        widget=forms.TextInput(attrs={'class' : 'form-input'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class' : 'form-input'})
    )

class UserRegisterForm(forms.Form):

    username = forms.CharField(
        label='Login or email',
        widget=forms.TextInput(attrs={'class' : 'form-input'})
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class' : 'form-input'})
    )
    password_checker = forms.CharField(
        label='Repeat password',
        widget=forms.PasswordInput(attrs={'class' : 'form-input'})
    )