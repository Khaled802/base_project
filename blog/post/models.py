
from tkinter.messagebox import NO
from django.db import models
from django.shortcuts import get_object_or_404, reverse
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    picture = models.ImageField(upload_to='images/')
    created_time = models.DateTimeField(auto_now_add=True)
    category=models.ForeignKey(Category , null = True , blank=True , on_delete=models.CASCADE , related_name='post_category')
    
    @classmethod
    def get_all_posts(cls):
        return cls.objects.all()

    @classmethod 
    def get_post(cls, id):
        print('hi')
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

    @classmethod
    def related_posts(cls , _category):
        return cls.objects.filter(category= _category)
    
    @classmethod
    def get_post_by_title(cls , passed_title):
        try:
            return cls.objects.get(title = passed_title)
        except:
            return None

       
class Tag(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return self.name

    @classmethod
    def get_all_tags(cls):
        return cls.objects.all()
    @classmethod
    def get_tag(cls , passed_tag):
        try:
            return Tag.objects.get(name = passed_tag)
        except:
            return None



class posts_tags(models.Model):
    post = models.ForeignKey(Post , related_name='posts_tags' , on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag , related_name='posts_tags' , on_delete=models.CASCADE)
    
    @classmethod
    def get_posts(cls , tag_name ):
        tag=Tag.get_tag(tag_name)
        try:
            return cls.objects.filter(tag=tag )
        except:
            return None

    @classmethod
    def get_tags(cls , post ):
        try:
            return cls.objects.filter(post=post)
        except:
            return None


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

    

