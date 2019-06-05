from django import forms
from django.contrib.auth.forms import ModelForm
from .models import Client

class ClientCreationForm(ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'phone_number']