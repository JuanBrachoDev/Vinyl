from django.contrib import admin
from .models import Order, OrderLineItem


# Admin display for Order Line Items
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


# Admin display for Orders
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'user_profile', 'order_date',
                       'delivery_cost', 'product_total',
                       'grand_total',)

    fields = ('order_number', 'order_date', 'user_profile', 'first_name',
              'last_name', 'email', 'phone_number',
              'county', 'eircode', 'city', 'address_line1',
              'address_line2', 'delivery_cost',
              'product_total', 'grand_total',)

    list_display = ('order_number', 'order_date', 'first_name', 'last_name',
                    'product_total', 'delivery_cost', 'grand_total',)

    ordering = ('-order_date',)


admin.site.register(Order, OrderAdmin)
