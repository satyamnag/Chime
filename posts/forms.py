from . models import *
from django import forms

class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title', 'image', 'caption')