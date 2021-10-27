from django.db import models
from django.urls import reverse
from datetime import date


# Create your models here.


# blogposts Model
class BlogPosts(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, default='auth.User',)
    title = models.CharField(max_length=100)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title + ' | ' + self.author.username

    def get_absolute_url(self):
        return reverse('blog')
