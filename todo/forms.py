from django import forms
from django.forms.forms import Form

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("user", "body",)
