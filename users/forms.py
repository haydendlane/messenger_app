from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'company') # , 'password1', 'password2')

class CustomUserChangeForm(UserChangeForm):
    password = None

    class Meta:
        model = Account
        fields = ('username', 'first_name', 'last_name', 'email', 'company') # , 'password1', 'password2')