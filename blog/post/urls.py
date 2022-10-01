
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import CreatePost,show_all_posts, show_post, like_post, unlike_post \
    , dislike_post, undislike_post

urlpatterns = [
    path('create/', CreatePost.as_view(), name='post.create'),
    path('show/', show_all_posts, name='post.show_all'),
    path('show/<int:id>', show_post, name='post.show'),
    path('like/<int:id>', like_post, name='post.like'),  
    path('unlike/<int:id>', unlike_post, name='post.unlike'),
    path('dislike/<int:id>', dislike_post, name='post.dislike'), 
    path('undislike/<int:id>', undislike_post, name='post.undislike'), 
]