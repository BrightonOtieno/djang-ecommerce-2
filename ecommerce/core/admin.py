from django.contrib import admin
from .models import Item,OrderItem,Order,Address,Payment,Coupon,Refund
# Register your models here.

# an action function (makes refund accepted)
# when a refund is accepted the request is set to False

def make_refund_accepted(modeladmin,request,queryset):
    queryset.update(refund_requested = False,refund_granted=True)

# a description of this action
make_refund_accepted.short_description = 'update Order to refund granted '


# display the Order table as a list of user  and ordered field
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user','ordered','being_delivered','received','refund_requested','refund_granted','billing_address','shipping_address','coupon','payment']
    list_display_links = ['billing_address','shipping_address','coupon','payment']

    list_filter = ['ordered','being_delivered','received','refund_requested','refund_granted']

    search_fields = [
        'user__username',
        'ref_code'
    ]

    # register our action
    actions = [make_refund_accepted]


# ADDRESS CUSTOMIZATION
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user','street_address','apartment_address','country',
        'zip_code','address_type','default'
    ]

    list_filter = ['default','address_type','country']

    search_fields = ['user','street_address','apartment_address','zip_code']

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order,OrderAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
