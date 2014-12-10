from django.conf.urls import patterns, include, url
from sapphire.home.views import home

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sapphire.views.home', name='home'),

    url(r'^$', home),
)
