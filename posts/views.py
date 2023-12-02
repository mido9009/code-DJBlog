from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForms

# Create your views here.


def post_list(request):
    data = Post.objects.all()
    context = {"object_list": data}
    return render(request, "posts/post_list.html", context)

def post_detial(request, pk):
    data = Post.objects.get(id=pk)
    context = {"post": data}
    return render(request, "posts/post_detial.html", context)


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

    return render(request, "posts/post_form.html", {"form": form})


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


