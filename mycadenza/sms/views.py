import os
from datetime import datetime, date

from django_twilio.decorators import twilio_view
from twilio.twiml import Response
from twilio.rest import TwilioRestClient
# from authy.api import AuthyApiClient

from signup.models import CadenzaUser

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', '')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', '')
TWILIO_PH_NO = os.environ.get('TWILIO_PH_NO', '')
AUTHY_API = os.environ.get('AUTHY_API', '')

@twilio_view
def sms(request):
    user_mobile = request.POST.get('From', '')
    user_in_db = CadenzaUser.objects.filter(mobile=user_mobile)
    response = Response()
    if user_in_db:
        user_msg = request.POST.get('Body', '')
        if user_msg.lower() == "today":
            now = datetime.now()
            client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
            todays_messages = client.messages.list(
                from_=user_mobile,
                to=TWILIO_PH_NO,
                date_sent=date(now.year, now.month, now.day)
            )
            todays_messages_body = "Here are all of your updates for today: "
            for message in todays_messages:
                todays_messages_body += message.body + ", "
            response.message(todays_messages_body)
        elif user_msg.lower() == "how to":
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
