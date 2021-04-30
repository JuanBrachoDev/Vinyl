from django.test import TestCase


class HomeViewsTestCase(TestCase):

    """
    Tests views in home app
    """

    def test_checkout(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertEqual(response.status_code, 200)
