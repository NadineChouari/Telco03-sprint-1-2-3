from django import forms
from django.forms import ModelForm
from forum.models import blog_posts

class PostsForm(forms.ModelForm):

    class Meta:
        model = blog_posts
        fields = ('id', 'title', 'author')

