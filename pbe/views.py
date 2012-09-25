from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User

def custom_proc(request):
    return  {
       'user': request.user,
       'ip_address': request.META['REMOTE_ADDR']
    }


def home(request):
    """
        Home screen of the portal.
    """
    return render_to_response('home.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


def artist(request, name):
    """
        Shows artist profile.
    """
    artist = User.objects.get(username = name)
    return render_to_response('artist.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


def list_artists(request):
    """
        Lists all the artists in the portal.
    """
    artists = User.objects.all()
    return render_to_response('artist_list.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


