from django.db import models
from users.models import Account
from django.urls import reverse
from django.core.validators import RegexValidator

'''
Client_ID (PK)  |       int
User_ID (FK)    |       int
First_Name      |       CharField(max_length=50)
Last_Name       |       CharField(max_length=50)
Phone           |       IntegerField(max_length=10)
'''

class Client(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '999999999'. Must be 10 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    # phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('client-detail', kwargs={'pk':self.pk})