from django.shortcuts import render

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

@twilio_view
def sms(request):
    user_phone = request.POST.get('From', '')
    user_msg = request.POST.get('Body', '')
    confirm_msg = user_phone
    response = Response()
    response.message(confirm_msg)
    return response
