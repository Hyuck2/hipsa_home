from django.shortcuts import render
from django.utils import timezone
from .models import Post

def home(request):
    posts = Post.objects.filter(updated__lte=timezone.now()).order_by('updated')
    return render(
        request,
        'blog/home.html',
        {
            'posts':posts
        }
    )
