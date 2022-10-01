from turtle import title
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import CustomUser
from django.urls import reverse_lazy
from .forms import UserRegister
from django.contrib.auth import logout
from django.contrib import messages

# Create your views here.
def user_register(request):
    if request.POST:
        form = UserRegister(request.POST)
        if form.is_valid():
             form.save()
             messages.success(request, 'create new account successfully')
             return redirect('login')
        else:
            messages.error(request, 'there is an error in inforamtion')
        
    new_form = UserRegister()
    return render(request, 'account/register.html', context={'form': new_form, title:'register'})

def user_profile(request):
    return render(request, 'account/profile.html', context={'title':'user'})


def show_profile(request, id):
    print( request.user, CustomUser.get_profile_id(id))
    if request.user == CustomUser.get_profile_id(id).user:
        return user_profile(request)
    profile =  CustomUser.get_profile_id(id)
    return render(request, 'account/show_profile.html', context={'title':profile.user, 'profile':profile})
    

def logout_view(request):
    logout(request)
    return redirect('login')