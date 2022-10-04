from django.db import models

# Create your models here.

class ForbiddenWord(models.Model):
    word = models.CharField(max_length=100)
    instead = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    @classmethod
    def get_all(cls) -> dict:
        dictionary = {}
        all_words = cls.objects.all()
        for forbidden_word in all_words:
            dictionary[forbidden_word.word] = forbidden_word.instead
        return dictionary

