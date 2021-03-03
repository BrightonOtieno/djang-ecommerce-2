from  django import template
from core.models import Order

register = template.Library()
# function that gets the count

@register.filter
def cart_item_count(user): # user is a Global variable
    if user.is_authenticated:
        qs = Order.objects.filter(user=user,ordered=False)
        if qs.exists():
            # pick the first incomplete order and return the count of items 
            order= qs[0]
            item_count = order.items.count()
            return item_count
    # if user is not authenticated/logged in
    return 0