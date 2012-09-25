from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('blog.views',
    url(r'submit/$', 'send_post'),
    url(r'blog/(?P<title>\w+)/$', 'show_post'),
    url(r'paintings/$', 'list_paintings'),
)
