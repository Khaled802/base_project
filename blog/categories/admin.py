from django.contrib import admin
from categories.models import Category 
from .models import Subscribe

# Register your models here.

admin.site.register(Category)
admin.site.register(Subscribe)


