from post.models import Post
from django import forms
from .models import ForbiddenWord

#changes here--------------------------------------------------------------------------
class PostModelForm(forms.ModelForm):
    tags=forms.CharField(max_length=100)
    class Meta:
        model=Post
        fields=['title' , 'details' , 'picture' , 'category' , 'tags']  

class EditForbiddenWord(forms.ModelForm):
    class Meta:
        model = ForbiddenWord
        fields = '__all__'