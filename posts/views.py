from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForms

# Create your views here.


"""def list_post(request):
    data = Post.objects.all()
    context = {"m": data}
    return render(request, "posts/list_post.html", context)"""


"""def post_detial(request, post_id):
    data = Post.objects.get(id=post_id)
    context = {"post": data}
    return render(request, "Posts/post_detial.html", context)"""


def create_post(request):
    if request.method == "POST":
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/posts/")
    form = PostForms()

    return render(request, "posts/new.html", {"form": form})


from django.views.generic import ListView, DetailView


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post
