from django.conf.urls import patterns, include, url
from pbe.views import home

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^home/$', home),
    url(r'^blog/', include('blog.urls')),
    url(r'^auth/', include('auth.urls')),
    # Examples:
    # url(r'^$', 'pbe.views.home', name='home'),
    # url(r'^pbe/', include('pbe.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
