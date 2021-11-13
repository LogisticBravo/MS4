""" Creates the contact view """
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from django.conf import settings
from .forms import ContactUsForm


# Create your views here.


def contact(request):
    """
    View for the contact form. Prepopulates with user details if signed in.
    Sends mail to developer with form details.
    Saves the form to the admin site.
    """
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = ContactUsForm(initial={'name': request.user.first_name,
                                          'email': request.user.email})

            context = {
                'form': form,
                }

            return render(request, 'contact/contact.html', context)

    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            subject = "Contact Us Form"
            body = {
                'Name': form.cleaned_data['name'],
                'Email': form.cleaned_data['email'],
                'Message': form.cleaned_data['message'],
            }
            message = '\n'.join(body.values())

            try:
                email = form.cleaned_data['email']
                send_mail(
                    subject,
                    message,
                    email,
                    [settings.DEFAULT_FROM_EMAIL]
                    )
            except BadHeaderError:
                return HttpResponse('Invalid Header')
            messages.success(request, 'Contact form submitted successfully.')
            return redirect('home')
        messages.error(request, "Error. Form not submitted.")
    else:
        form = ContactUsForm
    context = {
            'form': form,
        }

    return render(request, 'contact/contact.html', context)
