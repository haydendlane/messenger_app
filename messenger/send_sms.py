# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
from .models import Message
import os
import json

with open('/etc/config.json') as config_file:
    config = json.load(config_file)

TWILIO_ACCOUNT_SID = config['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = config['TWILIO_AUTH_TOKEN']

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send(user_id, user_company, client_id, client_phone_number):
    try:
        message = client.messages \
        .create(
            body='Thank you for visiting us at %s! Would you mind rating your experience by clicking on this link? https://google.com' % (user_company),
            from_='+14052941992',
            to='+1%i' % (client_phone_number),
            status_callback= 'http://45.79.26.50/api/delivery/'
        )

        save_message = Message(message_sid=message.sid,client=client_id,user=user_id,date_sent=message.date_created)
        save_message.save()
    except TwilioRestException as e:
        if 'not a valid phone number' in e.msg:
            raise Exception('The number was not valid.')
        else:
            raise
