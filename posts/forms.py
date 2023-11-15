from django import forms
from .models import Post


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("auth",)
        # fields = "__all__"
        # fields = []
