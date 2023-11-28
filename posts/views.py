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
            myform = form.save(commit=False)
            myform.auth = request.user
            myform.save()
            return redirect("/posts/")
    else:
        form = PostForms()

    return render(request, "posts/new.html", {"form": form})


def edit_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        form = PostForms(request.POST, request.FILES, instance=post)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.auth = request.user
            myform.save()
            return redirect("/posts/")
    else:
        form = PostForms(instance=post)

    return render(request, "posts/edit.html", {"form": form})


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect("/posts")


from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView


class PostList(ListView):
    model = Post


class PostDetail(DetailView):
    model = Post

class AddPost(CreateView):
    model = Post
    fields='__all__'
    success_url ='/posts/'

class Editpost(UpdateView):
    model = Post
    fields='__all__'
    success_url ='/posts/'
    template_name = 'posts/edit.html'