from django.shortcuts import render

from .models import Post

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})

def userpage(request):
    return render(request, 'blog/userpage.html')