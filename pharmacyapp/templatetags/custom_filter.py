from django import template
from decimal import Decimal

register = template.Library()

@register.filter(name="cart_quantity")
def cart_quantity(med_id, med_cart):
    keys = med_cart.keys()
    for id in keys:
        if int(id) == med_id.id:
            return med_cart.get(id)
    return False


@register.filter(name="total_cart_items")
def total_cart_items(items, med_cart):
    total_items = 0 
    for i in items:
        total_items += cart_quantity(i, med_cart)
    return total_items


@register.filter(name="cart_total")
def cart_total(med_id, med_cart):
    return med_id.selling_price * cart_quantity(med_id, med_cart)



@register.filter(name="get_grand_total")
def get_grand_total(items, cart):
    total = 0
    for i in items:
        total += cart_total(i, cart)
    return total