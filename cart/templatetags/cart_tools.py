from django import template

register = template.Library()


# Template filter that calculates de total value of
# a product based on its quantity and price
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity
