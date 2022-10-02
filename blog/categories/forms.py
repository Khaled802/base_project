from unicodedata import category
from categories.models import Category
from django import forms

class CategoryModelForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'