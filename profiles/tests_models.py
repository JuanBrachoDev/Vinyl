from django.test import TestCase
from .models import User


class ProfilesModelsTestCase(TestCase):

    """
    Helper functions
    """

    def user_example(self):
        test_user = {
            "first_name": "John",
            "last_name": "Doe",
            "address_line_1": "Hello",
            "address_line_2": "World",
            "city": "Yes",
            "county": "Dublin",
            "eircode": "1212 121",          
        }
        return test_user

    """
    Tests models in profiles app
    """

    def test_user(self):
        # Create test user from helper function and test user from Model
        user_1 = self.user_example()
        user_2 = User.objects.create(eircode="1212 121")
        # Compare both items for an eircode match
        self.assertEqual(
            user_1['eircode'],
            user_2.eircode
        )
