from django.shortcuts import render
from .forms import ContactUsForm

# Create your views here.


def contact(request):
    form = ContactUsForm

    context = {
            'form': form,
        }

    return render(request, 'contact/contact.html', context)
