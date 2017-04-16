from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from signup import views

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,{
                                        'template_name':'registration/logout.html'
                                        },
                                        name='logout'),
    url(r'^password_reset/$', auth_views.password_reset, {
                                'template_name': 'registration/password_reset.html'
                                },
                                name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
    url(r'^api/user/(?P<id>[0-9]+)/$', views.api_get_user, name="api_get_user"),
    url('', include('signup.urls')),
    url('', include('reports.urls')),
    url(r'^admin/', admin.site.urls),
    #twilio url
    url(r'^sms/$', views.sms, name='sms'),
]
