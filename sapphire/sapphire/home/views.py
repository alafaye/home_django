from django.shortcuts import render_to_response
from sapphire import settings

from sapphire.home.models import *
# Create your views here.


def home(request):
    # TODO news
    return render_to_response("home.html", dict(user=request.user, MEDIA_URL=settings.MEDIA_URL))
