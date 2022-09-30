from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import CustomUser
from django.urls import reverse_lazy
from .forms import UserRegister
from django.contrib.auth import logout

# Create your views here.
def user_register(request):
    if request.POST:
        form = UserRegister(request.POST)
        if form.is_valid():
             form.save()
             return redirect('post.show_all')
    new_form = UserRegister()
    return render(request, 'account/register.html', context={'form': new_form})

def user_profile(request):
    return render(request, 'account/profile.html', context={'title':'user'})

    

def logout_view(request):
    logout(request)
    return redirect('login')