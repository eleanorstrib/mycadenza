import os

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from twilio.rest import Client

from signup.models import CadenzaUser

ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', '')
AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', '')
TWILIO_PH_NO = os.environ.get('TWILIO_PH_NO', '')


@login_required
def dashboard(request):
    user = request.user
    print(user)
    user_data = CadenzaUser.objects.get(username=user)
    user_mobile_obj = user_data.mobile
    print('mobile', user_mobile_obj.country_code)
    user_mobile_no = "+" + str(user_mobile_obj.country_code) + str(user_mobile_obj.national_number)
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)
    all_entries = client.messages.list(
        from_=user_mobile_no,
        to=TWILIO_PH_NO,
    )
    all_entries_clean = [message for message in all_entries if message.body.lower() != 'today' and message.body.lower() != 'how to']
    print(all_entries_clean)
    return render(request, 'reports/dashboard.html', {'all_entries': all_entries_clean})
