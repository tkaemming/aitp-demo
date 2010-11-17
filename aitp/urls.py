from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(
        regex  = r'^$',
        view   = 'django.views.generic.simple.redirect_to',
        kwargs = {
            'url': '/blog/',
        }
    ),
    url(
        regex = r'^blog/',
        view  = include('aitp.blog.urls', namespace='blog'),
    ),
    url(
        regex = r'^comments/', 
        view  = include('django.contrib.comments.urls')
    ),
    url(
        regex = r'^admin/doc/', 
        view  = include('django.contrib.admindocs.urls')
    ),
    url(
        regex = r'^admin/', 
        view  = include(admin.site.urls)
    ),
)
