from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('auth.views',
    url(r'register/$', 'register'),
    url(r'login/$', 'login'),
    url(r'logout/$', 'logout'),
)
