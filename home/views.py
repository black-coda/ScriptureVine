from django.shortcuts import render
from .models import Post


## Implementing CRUD


def list_view(request):
    post = Post.objects.all()
    context = {
        'posts': post
    }
    return render(request, 'home/list_view.html', context)
