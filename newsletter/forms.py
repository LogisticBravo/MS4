from django import forms


class NewsletterForm(forms.Form):
    custom_names = {'email': 'newsletter_email'}

    def add_prefix(self, field_name):
        field_name = self.custom_names.get(field_name, field_name)
        return super(NewsletterForm, self).add_prefix(field_name)
        

    email = forms.EmailField(label='Your email',
                             max_length=100,
                             widget=forms.EmailInput(attrs={'class': 'form-control'}))
