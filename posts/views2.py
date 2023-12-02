from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from .models import Post

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

class DeletePost(DeleteView):
    model = Post
    success_url = '/posts/'