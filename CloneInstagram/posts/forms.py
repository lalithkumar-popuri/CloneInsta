from . import models
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        fields = ("image","caption")
        model = models.Post
