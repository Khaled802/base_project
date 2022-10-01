
from tkinter.messagebox import NO
from django.db import models
from django.shortcuts import get_object_or_404, reverse
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    picture = models.ImageField(upload_to='images/')
    created_time = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def get_all_posts(cls):
        return cls.objects.all()

    @classmethod 
    def get_post(cls, id):
        return get_object_or_404(cls, id=id)

    def get_post_url(self):
        return reverse('post.show', args=[self.id])


    def liked(self):
         return reverse('post.like', args=[self.id]) 
    
    def unliked(self):
        return reverse('post.unlike', args=[self.id]) 

    def disliked(self):
         return reverse('post.dislike', args=[self.id]) 
    
    def undisliked(self):
        return reverse('post.undislike', args=[self.id]) 

    def __str__(self) -> str:
        return self.title


class Like(models.Model):
    post = models.ForeignKey(Post, related_name='post_like', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_like', on_delete=models.CASCADE)

    @classmethod
    def get_like(cls, post, user):
        try:
            return cls.objects.get(post=post, user=user)
        except:
            return None

    @classmethod 
    def get_post_likes(cls,id): 
        return len(list(cls.objects.filter(post=id)))


class Dislike(models.Model):
    post = models.ForeignKey(Post, related_name='post_dislike', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_dislike', on_delete=models.CASCADE)

    @classmethod
    def get_dislike(cls, post, user):
        try:
            return cls.objects.get(post=post, user=user)
        except:
            return None

    @classmethod 
    def get_post_dislikes(cls,id): 
        return len(list(cls.objects.filter(post=id)))

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='post_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_comment', on_delete=models.CASCADE)
    comment_text = models.TextField()

    def __str__(self) -> str:
        return self.comment_text

    @classmethod
    def get_dislike(cls, post, user):
        try:
            return cls.objects.get(post=post, user=user)
        except:
            return None

