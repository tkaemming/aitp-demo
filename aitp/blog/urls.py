from django.conf.urls.defaults import *
from aitp.blog.feeds import LatestNewsFeed

urlpatterns = patterns('',
    url(
        regex = r'^$',
        view  = 'aitp.blog.views.post_list',
        name  = 'post_list',
    ),
    url(
        regex = r'^(?P<slug>[\w-]+)/$',
        view  = 'aitp.blog.views.post_detail',
        name  = 'post_detail',
    ),
    url(
        regex = r'^rss.xml$',
        view  = LatestNewsFeed(),
        name  = 'rss',
    ),
)