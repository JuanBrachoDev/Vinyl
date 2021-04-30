from django.test import TestCase
from .models import Products


class ProductsModelsTestCase(TestCase):

    """
    Helper functions
    """

    def product_example(self):
        product_example = {
            "name": "TestName",
            "genre": "Generic",
            "price": 99.99,
            "artist": "TheBest",
        }
        return product_example
        
    """
    Tests models in checkout app
    """

    def test_product(self):
        # Create test product from helper function and test product from Model
        product_1 = self.product_example()
        product_2 = Order.objects.create(genre="Generic")
        # Compare both items for a last name match
        self.assertEqual(
            product_1['genre'],
            product_2.genre
        )