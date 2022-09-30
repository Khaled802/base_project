from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='images/', default='default.gpj')
    bio = models.TextField(default='I am user')
    