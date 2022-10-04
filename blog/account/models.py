from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, reverse


# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(upload_to='images/', default='/images/default.png')
    bio = models.TextField(default='I am user')

    def get_profile_url(self):
        return reverse('account.show_profile', args=[self.id])

    @classmethod
    def get_profile_id(cls, id):
        return get_object_or_404(cls, pk=id)


