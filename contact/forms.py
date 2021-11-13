""" Contact us form module """
from django import forms
from .models import ContactUs

# Create a Contact Us form


class ContactUsForm(forms.ModelForm):
    """ Creates the contact us form using the model """
    class Meta:
        """ Sets all fields to be used from the model """
        model = ContactUs
        fields = '__all__'
