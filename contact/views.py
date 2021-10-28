from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages
from .forms import ContactUsForm


# Create your views here.


def contact(request):
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
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
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
