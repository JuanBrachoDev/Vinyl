from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from .models import Order, OrderLineItem
from products.models import Album
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    """
    A view for the checkout page that handles the payment
    """
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "cart": json.dumps(request.session.get("cart", {})),
                "save_info": request.POST.get("save_info"),
                "username": request.user,
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(
            request,
            "Sorry, your payment cannot be \
            processed right now. Please try again later.",
        )
        return HttpResponse(content=e, status=400)


def checkout(request):
    """
    A view for the checkout page that handles the order creation and form
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        cart = request.session.get("cart", {})
        # Collects form data
        form_data = {
            "first_name": request.POST["first_name"],
            "last_name": request.POST["last_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "address_line1": request.POST["address_line1"],
            "address_line2": request.POST["address_line2"],
            "city": request.POST["city"],
            "county": request.POST["county"],
            "eircode": request.POST["eircode"],
        }
        order_form = OrderForm(form_data)
        # Creates order if form is valid
        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get("client_secret").split("_secret")[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.save()
            for item_id, item_data in cart.items():
                try:
                    album = Album.objects.get(id=item_id)
                    order_line_item = OrderLineItem(
                        order=order,
                        product=album,
                        quantity=item_data,
                    )
                    order_line_item.save()
                except Album.DoesNotExist:
                    messages.error(
                        request,
                        (
                            "One of the albums in your cart wasn't found in our database. "
                            "Please call us for assistance!"
                        ),
                    )
                    order.delete()
                    return redirect(reverse("view_cart"))
            request.session["save_info"] = "save-info" in request.POST
            return redirect(reverse("checkout_success", args=[order.order_number]))
        else:
            messages.error(
                request,
                "There was an error with your form. \
                Please double check your information.",
            )
    else:
        cart = request.session.get("cart", {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment")
            return redirect(reverse("albums"))
        current_cart = cart_contents(request)
        total = current_cart["grand_total"]
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # Fills form with user info if available and user is logged in
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(
                    initial={
                        "first_name": profile.default_first_name,
                        "last_name": profile.default_last_name,
                        "email": profile.user.email,
                        "phone_number": profile.default_phone_number,
                        "address_line1": profile.default_address_line1,
                        "address_line2": profile.default_address_line2,
                        "city": profile.default_city,
                        "county": profile.default_county,
                        "eircode": profile.default_eircode,
                    }
                )
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()
    if not stripe_public_key:
        messages.warning(
            request,
            "Stripe public key is missing. \
            Did you forget to set it in your environment?",
        )
    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                "default_first_name": order.first_name,
                "default_last_name": order.last_name,
                "default_phone_number": order.phone_number,
                "default_address_line1": order.address_line1,
                "default_address_line2": order.address_line2,
                "default_city": order.city,
                "default_county": order.county,
                "default_eircode": order.eircode,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()
    messages.success(
        request,
        f"Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.",
    )

    if "cart" in request.session:
        del request.session["cart"]
    template = "checkout/checkout_success.html"
    context = {
        "order": order,
    }

    return render(request, template, context)
