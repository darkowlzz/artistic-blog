from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('blog.views',
    url(r'submit/$', 'send_post'),
    url(r'artists/$', 'list_artists'),
    url(r'blog/(?P<title>\w+)/$', 'show_post'),
    url(r'artist/(?P<name>\w+)/$', 'artist'),
)
