""" Set's up the newsletter form """
from django import forms


class NewsletterForm(forms.Form):
    """ sets up the newsletter form.
    Uses custom name and add prefix to differnetiate the form from others
    as it's persistant across the site.
    custom name of newsetter_email is used in the context logic to achieve this
    """
    custom_names = {'email': 'newsletter_email'}

    def add_prefix(self, field_name):
        field_name = self.custom_names.get(field_name, field_name)
        return super(NewsletterForm, self).add_prefix(field_name)

    email = forms.EmailField(label='Your email',
                             max_length=100,
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control'
                                 }))
