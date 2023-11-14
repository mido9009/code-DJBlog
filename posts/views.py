from django.shortcuts import render
from .models import Post

# Create your views here.


"""def list_post(request):
    data = Post.objects.all()
    context = {"m": data}
    return render(request, "posts/list_post.html", context)"""


"""def post_detial(request, post_id):
    data = Post.objects.get(id=post_id)
    context = {"post": data}
    return render(request, "Posts/post_detial.html", context)"""

from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post   