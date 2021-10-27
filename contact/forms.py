from django import forms
from .models import ContactUs

# Create a Contact Us form
class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = '__all__'
