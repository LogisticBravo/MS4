from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    """
    View to get bag from the seesion. If not redirects to product pager and
    prohibits people from accessing checkout page otherwise.
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JVLAUFlFfTxzZDIFaVv8Z2FFCniDH9uwvveVAYMgNGkOasUUsNOsOYC98ygt9lrOBIGxOSCpFgAv5ugKbKagNZ700szzHd5YM',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
