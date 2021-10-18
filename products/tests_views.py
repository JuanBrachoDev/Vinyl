from django.test import TestCase
from .models import Products


class ProductsViewsTestCase(TestCase):

    """
    Tests views in cart app
    """

    def test_products(self):
        response = self.client.get('/products/')
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(response.status_code, 200)
   
    def test_product_details(self):
        response = self.client.get('/products/1')
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertEqual(response.status_code, 200)
