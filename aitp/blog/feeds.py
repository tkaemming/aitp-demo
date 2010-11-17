from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from aitp.blog.models import Post

class LatestNewsFeed(Feed):
    title = "AITP Demonstration Latest News"
    link = lambda self: reverse('blog:post_list')
    description = "The latest news from the AITP Demonstration project."

    def items(self):
        return Post.objects.all()[0:10]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content