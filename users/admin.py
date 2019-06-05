from .forms import UserCreationForm, UserChangeForm
from .models import Account
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django import forms
from django.contrib import admin

class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = Account
    list_display = ['username', 'email', 'first_name', 'last_name', 'company']

admin.site.register(Account, CustomUserAdmin)