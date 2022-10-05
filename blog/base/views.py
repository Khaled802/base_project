from django.shortcuts import render

# Create your views here.

def show_about(request):
    return render(request , 'base/about.html')