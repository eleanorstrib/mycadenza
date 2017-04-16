from django.shortcuts import render

from django_twilio.decorators import twilio_view
from twilio.twiml import Response


def dashboard(request):
    return render(request, 'reports/dashboard.html', {})

@twilio_view
def sms(request):
    user_msg = request.POST.get('Body', '')
    confirm_msg = "Thanks!  Your entry has been recorded on Cadenza.""
    empty_msg = "Hmm. The entry you sent is empty.  Try again?"
    r = Response()
    if user_msg != '':
        r.message(confirm_msg)
    else:
        r.message(empty_msg)
    return r
