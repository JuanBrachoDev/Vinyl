from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Album


def cart_contents(request):

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    # Adds each item's id, quantity and album to cart_items
    for item_id, quantity in cart.items():
        album = get_object_or_404(Album, pk=item_id)
        if album.special_offer_price:
            total += quantity * album.special_offer_price
        else:
            total += quantity * album.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'album': album,
        })

    # Calculates delivery fee
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    # Grand total
    grand_total = delivery + total

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context
