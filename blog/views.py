from django.http import HttpRequest, Http404
from django.shortcuts import render

from blog.models import Post


# Create your views here.
def list_posts(request: HttpRequest):
    posts = Post.published.all()
    return render(request=request, template_name='blog/post/list.html', context={'posts': posts})

def post_detail(request: HttpRequest, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404

    return render(request=request, template_name='blog/post/detail.html', context={'post': post})