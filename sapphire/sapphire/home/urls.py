from django.conf.urls import patterns, include, url
from sapphire.home.views import index

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sapphire.views.home', name='home'),

    url(r'^$', index),
)
