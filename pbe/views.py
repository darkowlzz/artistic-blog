from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def custom_proc(request):
    return  {
       'user': request.user,
       'ip_address': request.META['REMOTE_ADDR']
    }


def home(request):
    return render_to_response('home.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))
