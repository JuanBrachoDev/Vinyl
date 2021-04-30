from django.test import TestCase
from datetime import date


class CheckoutViewsTestCase(TestCase):

    """
    Helper functions
    """

    def order_example(self):
        test_order = {
            "order_id": "8957158459",
            "user": 5,
            "first_name": "John",
            "last_name": "Doe",
            "email": "test@email.com",
            "address_line_1": "Hello",
            "address_line_2": "World",
            "city": "Yes",
            "county": "Dublin",
            "eircode": "1111 222",
            "order_date": datetime.now(),
            "delivery_cost": 9.99,
            "product_cost": 90.00,
            "grand_total": 99.99,            
        }
        return test_order

    """
    Tests views in checkout app
    """

    def test_checkout(self):
        response = self.client.get('/checkout/')
        self.assertTemplateUsed(response, 'checkout/checkout.html')
        self.assertEqual(response.status_code, 200)

    def test_checkout_success(self):
        with self.subTest:
