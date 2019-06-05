# from django.db import models
# from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import AbstractUser

class Account(AbstractUser):
    company = models.CharField(max_length=100)

    def __str__(self):
        return self.username

# '''
# User_ID (PK)    |       int
# User            |       CharField(User, on_delete=models.CASCADE)
# Email           |       EmailField(max_length=100)
# Company         |       CharField(max_length=50)
# '''

# class Account(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     email = models.EmailField(max_length=100)
#     company = models.CharField(max_length=50)

#     def __str__(self):
#         return f'{self.user.username} Profile'