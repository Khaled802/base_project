from post.models import Post
from django import forms

#changes here--------------------------------------------------------------------------
class PostModelForm(forms.ModelForm):
    tags=forms.CharField(max_length=100)
    class Meta:
        model=Post
        fields=['title' , 'details' , 'picture' , 'category' , 'tags']  