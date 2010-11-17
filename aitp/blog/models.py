from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey('auth.User')
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    
    # This returns a string representation of the object, good for use in the 
    # interactive shell, as well as any time the object is cast to a string.
    def __unicode__(self):
        # Notice that you have to explicitly pass "self" to any instance methods.
        return '%s' % self.title
    
    @models.permalink
    def get_absolute_url(self):
        """Returns the absolute URL to this blog post."""
        return ('blog:post_detail', (), {'slug': self.slug})
    url = property(get_absolute_url)