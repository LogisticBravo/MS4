from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail

from .models import NewsletterSignups
from .forms import NewsletterForm


@csrf_exempt
def newsletter(request):
    """ A view to capture users email addresses, send an email and
        add the email address to the newsletter database
    """
    email = ''
    form = NewsletterForm(request.POST or None)

    if 'newsletter_email' in request.POST:
        try:
            email = request.POST['newsletter_email']
            signup = NewsletterSignups(email=email)
        except KeyError:
            signup = 'Your Email'

        if form.is_valid():
            email = request.POST['newsletter_email']
            if NewsletterSignups.objects.filter(email=email).exists():
                messages.error(request, "Eager! You've already signed up!")
            else:
                signup.save()
                messages.success(request, f'Thanks! {email} added to mailing list!')

                subject = render_to_string(
                    'newsletter/confirmation_emails/newsletter_confirmation_email_subject.txt',
                    )
                body = render_to_string(
                    'newsletter/confirmation_emails/newsletter_confirmation_email_body.txt',
                    {'contact_email': settings.DEFAULT_FROM_EMAIL})

                send_mail(
                    subject,
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [signup]
                )

        # redirect_url = request.POST.get('home')

        context = {
            'newsletter_form': NewsletterForm,
        }

        return context
    else:
        if request.user.is_authenticated:
            if request.method == 'GET':
                form = NewsletterForm(initial={'email': request.user.email})

            context = {
                    'newsletter_form': form,
                }
            return context
        else:
            context = {
                'newsletter_form': NewsletterForm,
            }
            return context
