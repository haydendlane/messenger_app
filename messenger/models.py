from django.db import models
from users.models import Account
from clients.models import Client
from django.utils import timezone

'''
Message_ID (PK) |       int
Client_ID (FK)  |       int
User_ID (FK)    |       int
Date_Sent       |       DateTime
'''

class Message(models.Model):
    message_sid = models.CharField(max_length=250, primary_key=True, default='SID')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    date_sent = models.DateTimeField(default=timezone.now)
    delivery_status = models.CharField(max_length=100, default='unsent')

    def __str__(self):
        return f'{self.message_sid}: {self.client} {self.date_sent}'
