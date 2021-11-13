""" Creates the newsletter model """
from django.db import models


# Create your models here.

class NewsletterSignups(models.Model):
    """ sets up the email """
    email = models.EmailField(unique=True)

    class Meta:
        """ sets plural name for admin site """
        verbose_name_plural = "Newsletter Sign-up's"

    def __str__(self):
        return self.email
