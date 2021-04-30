from django.test import TestCase
from .forms import OrderForm


class CheckoutFormsTestCase(TestCase):

    """
    Tests forms in checkout app
    """

    def test_form(self):
        form = OrderForm({
            "first_name": "",
            "last_name": "",
            "email": "",
            "address_line_1": "",
            "address_line_2": "",
            "city": "",
            "county": "",
            "eircode": "",
            })
        
        # Tests required fields
        self.assertEqual(
            form.errors['first_name'][0], 'This is a required field.')
        self.assertEqual(
            form.errors['last_name'][0], 'This is a required field.')
        self.assertEqual(
            form.errors['email'][0], 'This is a required field.')
        self.assertEqual(
            form.errors['address_line_1'][0], 'This is a required field.')
        self.assertEqual(
            form.errors['city'][0], 'This is a required field.')
        self.assertEqual(
            form.errors['county'][0], 'This is a required field.')
        self.assertEqual(
            form.errors['eircode'][0], 'This is a required field.')
        
        # Makes sure form is invalid
        self.assertFalse(form.is_valid())
