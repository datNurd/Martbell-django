from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url('^register/$',views.register, name='register'),
    url('^login/$',views.login_merchant, name='login'),
    url('^pannel/$', views.pannel, name='merchant_pannel'),
    url('^logout/$', views.logout_merchant, name='logout'),
)
