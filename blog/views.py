from django.shortcuts import redirect, render
from django.contrib.auth import login
from .models import *
from .forms import RegistrationUserForm
from django.contrib.auth.decorators import login_required

def frontpage(request):
    posts = Post.objects.all()

    return render(request, 'blog/frontpage.html', {'posts': posts})

def regpage(request):
    if request.method == 'POST':
        form = RegistrationUserForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('frontpage')              

    else:
        form = RegistrationUserForm()    

    return render(request, 'blog/regpage.html', {'form':form})

def loginpage(request):
    return render(request, 'blog/login.html', )

def userpage(request):
    return render(request, 'blog/userpage.html', )



