from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


# A view that shows the checkout form and a summary of the order
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': "pk_test_51IgSBBCXlFoUp4sYfShIp9c3ZxHLABdmDKDIFCPPWhJIOQ0y67YAIOk0QchxMYGpSJQxZ6Q84tyG6Wpzoyjm4Glu00bF4sXhcL",
        'client_secret': 'test_client_secret'
    }

    return render(request, template, context)
