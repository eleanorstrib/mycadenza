from django.shortcuts import render

# from django_twilio.decorators import twilio_view
from twilio import twiml

# @twilio_view
def sms(request):
    # pass
    user_msg = request.POST.get('Body', '')
    confirm_msg = "Thanks!  Your entry has been recorded on Cadenza."
    empty_msg = "Hmm. The entry you sent is empty.  Try again?"
    response = twiml.Response()
    if user_msg != '':
        response.message(confirm_msg)
    else:
        response.message(empty_msg)
    return r
