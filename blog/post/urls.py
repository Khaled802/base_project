
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CreatePost,show_all_posts, show_post

urlpatterns = [
    path('create/', CreatePost.as_view(), name='post.create'),
    path('show/', show_all_posts, name='post.show_all'),
    path('show/<int:id>', show_post, name='post.show'),
    
]