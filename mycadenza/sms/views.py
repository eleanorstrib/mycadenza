from django.shortcuts import render

from django_twilio.decorators import twilio_view
from twilio.twiml import Response

from signup.models import CadenzaUser


@twilio_view
def sms(request):
    user_mobile = request.POST.get('From', '')
    user_in_db = CadenzaUser.objects.filter(mobile=user_mobile)
    response = Response()
    if user_in_db:
        user_msg = request.POST.get('Body', '')
        response.message("Thank you - your entry has been recorded.")
    else:
        response.message(
            "You have the wrong number - please remove this one from your phone."
            )
    return response
