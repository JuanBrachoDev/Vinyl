from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Album


# A view that shows the shopping cart's contents
def view_cart(request):
    """A view that renders the cart contents page"""

    return render(request, "cart/cart.html")


# Adds the selected item to the shopping cart
def add_to_cart(request, item_id):
    """Add a quantity of the specified product to the shopping cart"""

    album = get_object_or_404(Album, pk=item_id)

    # Returns 404 if an invalid quantity is entered
    try:
        quantity = int(request.POST.get("quantity"))
    except Exception as e:
        return HttpResponse(status=404)
    redirect_url = request.POST.get("redirect_url")
    cart = request.session.get("cart", {})

    # Adds quantity to existing cart item or adds set quantity to cart
    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f"Updated {album.name} quantity to {cart[item_id]}")
    else:
        cart[item_id] = quantity
        messages.success(request, f"Added {album.name} to your cart.")
    request.session["cart"] = cart
    return redirect(redirect_url)


# Modifies the selected item in the shopping cart
def adjust_cart(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    album = get_object_or_404(Album, pk=item_id)

    # Returns 404 if an invalid quantity is entered
    try:
        quantity = int(request.POST.get("quantity"))
    except Exception as e:
        return HttpResponse(status=404)
    cart = request.session.get("cart", {})

    # Updates quantity of existing cart item or removes from cart if quantity < 0  
    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f"Updated {album.name} quantity to {cart[item_id]}")
    else:
        cart.pop(item_id)
        messages.success(request, f"Removed {album.name} from your cart.")
    request.session["cart"] = cart
    return redirect(reverse("view_cart"))


# Removes the selected item from the shopping cart
def remove_from_cart(request, item_id):
    """Remove the item from the shopping cart"""

    try:
        cart = request.session.get("cart", {})
        album = get_object_or_404(Album, pk=item_id)
        # Removes item from cart if able or returns 404
        if album:
            cart.pop(item_id)
            messages.success(request, f"Removed {album.name} from your cart.")
            request.session["cart"] = cart
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
    except Exception as e:
        messages.error(request, f"Error removing item: {e}")
        return HttpResponse(status=500)
