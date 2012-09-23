from django.shortcuts import render_to_response
from pbe.views import custom_proc
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib import auth
from auth.forms import RegisterForm, LoginForm

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            c = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
            c.save()

            title = "Account Created Successfully!!"
            string = title
            return render_to_response('success.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))
    else:
        form = RegisterForm()
    return render_to_response('registration.html', {'form': form}, context_instance=RequestContext(request, processors=[custom_proc]))


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = auth.authenticate(username=cd['username'], password=cd['password'])
            if user is not None and user.is_active:
                auth.login(request, user)
                return render_to_response('home.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))
    else:
        form = LoginForm()
    return render_to_response('login.html', {'form': form}, context_instance=RequestContext(request, processors=[custom_proc]))


def logout(request):
    auth.logout(request)
    title = "Logged out!!"
    string = title
    return render_to_response('success.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


