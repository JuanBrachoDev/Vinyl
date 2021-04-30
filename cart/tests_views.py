from django.test import TestCase
from products.models import Product
from django.shortcuts import get_object_or_404


class CartViewsTestCase(TestCase):

    """
    Helper functions
    """

    def vinyl_example(self):
        test_album = {
            "name": "TestName",
            "genre": "Generic",
            "price": 99.99,
            "artist": "TheBest",
        }
        return test_album

    """
    Tests views in cart app
    """

    def test_cart(self):
        response = self.client.get('/cart/')
        self.assertTemplateUsed(response, 'cart/cart.html')
        self.assertEqual(response.status_code, 200)

    def test_add_to_cart(self):
        with self.subTest:
            # Post test album
            response = self.app.post(
                "/add_to_cart", data=self.vinyl_example(),
                follow_redirects=True
            )
            # Check if posted album exists in response
            assert("TestName" in response.data)

    def test_adjust_cart(self):
        with self.subTest:
            # Post test album
            self.app.post(
                "/add_to_cart", data=self.vinyl_example(),
                follow_redirects=True
            )
            product = get_object_or_404(Product, pk=item_id)
            # Adjust quantity to 4
            response = self.app.post("/adjust_cart", product.item_id, {
                "quantity": 4,
            })
            # Check album quantity was updated to 4
            assert(4 in response)

    def test_delete_from_cart(self):
        with self.subTest:
            # Post test album
            self.app.post(
                "/add_to_cart", data=self.vinyl_example(),
                follow_redirects=True
            )
            product = get_object_or_404(Product, pk=item_id)
            # Remove test album from cart
            response = self.app.post("/remove_from_cart", product.item_id)
            assert("TestName" not in response)
