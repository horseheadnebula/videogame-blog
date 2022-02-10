from django.shortcuts import render
from users.models import CustomUser
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})

def regpage(request):
    form = RegistrationUserForm()
    return render(request, 'blog/regpage.html', { 'form':form })

def loginpage(request):
    return render(request, 'blog/login.html', )

def userpage(request):
    user = CustomUser.objects.all()
    return render(request, 'blog/userpage.html', {'user': user})



