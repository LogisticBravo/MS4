""" Creaes the Contact us model """
from django.db import models

# Create your models here.


class ContactUs(models.Model):
    """ Set's up the fields for the contact us form """
    name = models.CharField('Name', max_length=254)
    email = models.EmailField('Email', max_length=254)
    message = models.TextField('Message', max_length=2000)

    class Meta:
        """ Sets the plural name for admin site """
        verbose_name_plural = "Contact Forms"

    def __str__(self):
        return self.name + ' | ' + self.email
