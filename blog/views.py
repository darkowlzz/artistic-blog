from django.shortcuts import render_to_response
from pbe.views import custom_proc
from django.template import RequestContext
from blog.forms import PostForm
from blog.models import Post
from django.contrib.auth.models import User


def send_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            t = ''
            cd['title'] = cd['title'].replace(" ", "_")
            #x = cd['title'].split()
            #cd['title'] = t.join(x)
            p = Post(user=request.user, title=cd['title'], text=cd['text'])
            p.save()

            title = "Posted successfully"
            string = "Your post has been submitted successfully."
            return render_to_response('success.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))
    else:
        form = PostForm()
    return render_to_response('post.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


def list_artists(request):
    artists = User.objects.all()[1:]
    return render_to_response('artist_list.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))

def artist(request, name):
    artist = User.objects.get(username=name)
    return render_to_response('artist.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))

def show_post(request, title):
    p = Post.objects.get(title=title)
    title = title.replace("_", " ")
    return render_to_response('read.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))
