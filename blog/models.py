from django.db import models
from django.urls import reverse


# Create your models here.


# blogposts Model
class BlogPosts(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='auth.User',)
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog')
