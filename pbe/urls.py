from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('pbe.views',
    url(r'^$', 'home'),
    url(r'^home/$', 'home'),
    url(r'^artists/$', 'list_artists'),  
    url(r'^(?P<name>\w+)/$', 'artist'),   # ordering matters, this should be at the end

    url(r'^blog/', include('blog.urls')),
    url(r'^auth/', include('auth.urls')),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
