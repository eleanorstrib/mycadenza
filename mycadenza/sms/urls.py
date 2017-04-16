from django.conf.urls import url
from sms import views

urlpatterns = [
    #twilio url
    url(r'^$', views.sms, name='sms'),
]
