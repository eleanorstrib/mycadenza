from django.shortcuts import render

from twilio import twiml
from django_twilio.decorators import twilio_view

@twilio_view
def sms(request):
    user_msg = request.POST.get('Body', '')
    confirm_msg = "Thanks!  Your entry has been recorded on Cadenza."
    response = twiml.Response()
    response.message(confirm_msg)
    return response
