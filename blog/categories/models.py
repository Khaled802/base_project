from django.db import models
from django.shortcuts import get_object_or_404, reverse
from account.models import CustomUser
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    picture = models.ImageField(upload_to='images/')
    created_time = models.DateTimeField(auto_now_add=True)
    
    @classmethod
    def get_all_categories(cls):
        return cls.objects.all()

    @classmethod 
    def get_category(cls, id):
        return get_object_or_404(cls, id=id)

    def get_category_url(self):
        return reverse('category.show', args=[self.id])

    def get_subscribe_url(self):
        return reverse('category.subscribe', args=[self.id])
    
    def get_subscribers(self):
        return set([sub.user for sub in Subscribe.objects.filter(category=self)])


    def __str__(self) -> str:
        return self.title

class Subscribe(models.Model):
    user = models.ForeignKey(User , related_name='user_subscribe' , on_delete=models.CASCADE)
    category = models.ForeignKey(Category , related_name='category_subscribe' , on_delete=models.CASCADE)

    @classmethod
    def get_subscribe(cls , category , user):
        try:
            return cls.objects.get(category=category , user=user)
        except:
            return None

   
    @classmethod
    def get_all_subscriptions(cls):
        return cls.objects.all()