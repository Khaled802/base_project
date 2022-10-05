from email.policy import default
from django.db import models
from django.urls import reverse
# Create your models here.

class ForbiddenWord(models.Model):
    word = models.CharField(max_length=100)
    instead = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return self.title

    @classmethod
    def get_all(cls) -> dict:
        dictionary = {}
        all_words = cls.objects.all()
        for forbidden_word in all_words:
            dictionary[forbidden_word.word] = forbidden_word.instead
        return dictionary

    def delete_forbiddenword_url(self):
        return reverse('delete_forbiddenword', args=[self.id])

    def update_forbiddenword_url(self):
        return reverse('update_forbiddenword', args=[self.id])
