""" Creates the blogposts model """
from django.urls import reverse
from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class BlogPosts(models.Model):
    """ Model for Blogposts """
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               default=User,)
    title = models.CharField(max_length=100)
    body = models.TextField()
    published_date = models.DateField(auto_now_add=True)

    class Meta:
        """ plural name for django admin site """
        verbose_name_plural = "Blog Posts"

    def __str__(self):
        return self.title + ' | ' + self.author

    def get_absolute_url(self):
        """ converst to an absolute url """
        return reverse('blog')
