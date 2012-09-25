from django.shortcuts import render_to_response
from pbe.views import custom_proc
from django.template import RequestContext
from blog.forms import PostForm
from blog.models import Post
from django.contrib.auth.models import User

noise = [',', "'", '"', '.', ';', ':', ' ']  # to be used in title conversion

def send_post(request):
    """Handles Blog Posting Form"""

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cd['title'] = title_conversion(cd['title'])
            # cd['title'] = cd['title'].replace(" ", "_")  

            p = Post(user=request.user, title=cd['title'], text=cd['text'])
            p.save()
            
            # content to be displayed in success page
            title = "Posted successfully"
            string = "Your post has been submitted successfully."
            return render_to_response('success.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))
    else:
        form = PostForm()
    return render_to_response('post.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


def title_conversion(title):
    """
        Gets a title string and replaces all the url error causing character with '_' 
        Returns the new title.
    """

    title = list(title)
    for i in range(len(title)):
        if title[i] in noise:
            title[i] = '_'

    return ''.join(i for i in title)


def list_artists(request):
    artists = User.objects.all()

    return render_to_response('artist_list.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


def artist(request, name):
    artist = User.objects.get(username=name)
    return render_to_response('artist.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


def show_post(request, title):
    """
        Gets the required post and displays it
    """
    p = Post.objects.get(title=title)
    title = title.replace("_", " ")
    return render_to_response('read.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))


def list_paintings(request):
    """
        Lists all the posts in the system
    """
    paintings = Post.objects.order_by('-time')
    return render_to_response('paintings.html', locals(), context_instance=RequestContext(request, processors=[custom_proc]))

