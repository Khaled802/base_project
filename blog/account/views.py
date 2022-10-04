from turtle import title
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from .models import CustomUser
from django.urls import reverse_lazy, reverse
from .forms import UserRegister, EditProfile
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.models import User
from django import views

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
    try:
        request.user.profile
    except:
        create_profile(request.user)
    
    if request.POST:
        edit = request.user.profile
        print(request.POST)
        form  = EditProfile(request.POST, request.FILES, instance=edit)
        form.save()
        return redirect(reverse('account.profile'))

    edit = request.user.profile
    new_form = EditProfile(instance=edit)
    return render(request, 'account/profile.html', context={'title':request.user, 'form':new_form})


def show_profile(request, id):
    print( request.user, CustomUser.get_profile_id(id))
    if request.user == CustomUser.get_profile_id(id).user:
        return user_profile(request)
    profile =  CustomUser.get_profile_id(id)
    return render(request, 'account/show_profile.html', context={'title':profile.user, 'profile':profile})
    

def logout_view(request):
    logout(request)
    return redirect('login')



def create_profile(user):
    profile = CustomUser()
    profile.user = user
    profile.save()






