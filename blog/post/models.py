
from django.db import models
from django.shortcuts import get_object_or_404, reverse

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


    def __str__(self) -> str:
        return self.title

