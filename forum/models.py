from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse



# Create your models here.
class blog_posts(models.Model):
    title = models.CharField(max_length=400)
    content = models.CharField(max_length=50)
    author = models.CharField(max_length=120)
    def __str__(self):
        return self.title


    def get_post_url(self):
        return reverse('post_edit', kwargs={'pk': self.pk})