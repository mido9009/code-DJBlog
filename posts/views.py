from django.shortcuts import render
from .models import Post

# Create your views here.


def list_post(request):
    data = Post.objects.all()
    context = {"m": data}
    return render(request, "posts/list_post.html", context)


def post_detial():
    pass
