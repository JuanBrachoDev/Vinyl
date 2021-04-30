from django.test import TestCase
from datetime import date
from .models import Order, OrderLineItem


class CheckoutTestCase(TestCase):

    """
    Helper functions
    """

    def order_example(self):
        test_order = {
            "order_id" : "8957158459",
            "user" : 5,
            "first_name" : "John",
            "last_name" : "Doe",
            "email" : "test@email.com",
            "address_line_1" : "Hello",
            "address_line_2" : "World",
            "city" : "Yes",
            "county" : "Dublin",
            "eircode" : "1111 222",
            "order_date" : datetime.now(),
            "delivery_cost" : 9.99,
            "product_cost" : 90.00,
            "grand_total" : 99.99,            
        }
        return test_order

    def order_line_example(self):
        test_order_line = {
            "order" = 2,
            "album" = 4,
            "quantity" = 2,
            "total" = 120.99
        }

    """
    Tests views in cart app.
    """

    def test_order(self):
        # Create test order from helper function and test order from Model
        order_1 = self.order_example()
        order_2 = Order.objects.create(last_name="Doe")
        # Compare both items for a last name match
        self.assertEqual(order_line_item_1['last_name'], order_line_item_2.last_name)

    def test_order_line_item(self):
        # Create test order line item from helper function 
        # and test order line item from Model
        order_line_item_1 = self.order_line_example()
        order_line_item_2 = Order.objects.create(album=4)
        # Compare both items for an album match
        self.assertEqual(order_line_item_1['album'], order_line_item_2.album)
            