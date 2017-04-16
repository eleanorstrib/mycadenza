import os
import datetime

from django.shortcuts import render

from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from twilio.rest import TwilioRestClient

from signup.models import CadenzaUser

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', '')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', '')
TWILIO_PH_NO = os.environ.get('TWILIO_PH_NO', '')


@twilio_view
def sms(request):
    user_mobile = request.POST.get('From', '')
    user_in_db = CadenzaUser.objects.filter(mobile=user_mobile)
    response = Response()
    if user_in_db:
        user_msg = request.POST.get('Body', '')
        if user_msg.lower() == "today":
            now = datetime.datetime.now()
            client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
            todays_messages = client.messages.list(
                date_sent=datetime.date(now.year, now.month, now.day)
            )
            response.message(todays_messages)
        elif user_msg.lower() == "info":
            response.message(
                "Type 'today' for all of your current entries. To add an entry, text anything else!"
            )
        else:
            response.message("Thank you - your entry has been recorded.")
    else:
        response.message(
            "You have the wrong number - please remove this one from your phone."
            )
    return response
