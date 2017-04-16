from django.conf.urls import url
from . import views

urlpatterns = [
    #twilio url
    url(r'^sms$', views.sms, name='sms'),
]
