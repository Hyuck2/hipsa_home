from django import forms
from .models import Post

class PostForm(forms.MdoelFrom):

    class Meta:
        model = Post
        fileds = ('title', 'text',)