from django.db import models


# Create your models here.

class NewsletterSignups(models.Model):
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name_plural = "Newsletter Sign-up's"

    def __str__(self):
        return self.email
