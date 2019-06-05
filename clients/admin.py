from django.contrib import admin
from .models import Client

class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone_number')

# Register your models here.

admin.site.register(Client, ClientAdmin)