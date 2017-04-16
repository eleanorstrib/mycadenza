from django.shortcuts import render

from twilio import twiml
from django_twilio.decorators import twilio_view
#
# @twilio_view
def sms(request):
    user_msg = request.POST.get('Body', '')
    confirm_msg = "Thanks!  Your entry has been recorded on Cadenza."
    empty_msg = "Hmm. The entry you sent is empty.  Try again?"
    response = twiml.Response()
    if user_msg != '':
        response.message(confirm_msg)
    else:
        response.message(empty_msg)
    return response
