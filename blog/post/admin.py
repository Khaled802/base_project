from django.contrib import admin
from .models import Post, Like, Dislike, Comment, Tag, posts_tags

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(posts_tags)

