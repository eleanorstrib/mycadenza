from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.signup, name='home'),
    url(r'^change_password/$', views.change_password, name='change_password'),
]
