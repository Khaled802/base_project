from django.urls import path
from admn.views import \
show_dashboard,list_of_users,be_admin,block_user,unblock_user,list_of_posts,delete_post,edit_post,create_post,view_post,\
like_post,unlike_post,dislike_post,undislike_post, AddForbiddenWord, delete_forbiddenword, update_forbidden_words



urlpatterns = [
    path('show_dashboard',show_dashboard,name='show_dashboard'),
    path('list_of_users',list_of_users,name='list_of_users'),
    path('be_admin/<int:id>',be_admin,name='be_admin'),
    path('block_user/<int:id>',block_user,name='block_user'),
    path('unblock_user/<int:id>',unblock_user,name='unblock_user'),
    path('list_of_posts',list_of_posts,name='list_of_posts'),
    path('CreatePost', create_post, name='CreatePost'),
    path('view_post/<int:id>', view_post, name='view_post'),
    path('delete_post/<int:id>',delete_post,name='delete_post'),
    path('edit/<int:id>', edit_post, name='edit_post'),

    path('like_post/<int:id>', like_post, name='like_post'),  
    path('unlike_post/<int:id>', unlike_post, name='unlike_post'),
    path('dislike_post/<int:id>', dislike_post, name='dislike_post'), 
    path('undislike_post/<int:id>', undislike_post, name='undislike_post'),


     path('add_forbiddenword/', AddForbiddenWord.as_view(), name='add_forbiddenword'),
     path('delete_forbiddenword/<int:id>', delete_forbiddenword, name='delete_forbiddenword'),
     path('update_forbiddenword/<int:id>', update_forbidden_words , name='update_forbiddenword')

    
]

