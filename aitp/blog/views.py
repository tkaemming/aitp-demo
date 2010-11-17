from django.views.generic.list_detail import object_detail, object_list
from aitp.blog.models import Post

def post_list(request):
    return object_list(
        request = request,
        queryset = Post.objects.all(),
    )

def post_detail(request, slug):
    return object_detail(
        request = request,
        queryset = Post.objects.all(),
        slug = slug
    )