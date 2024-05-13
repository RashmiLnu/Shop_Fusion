# test_home.py

from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Product

class HomeViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')

        with open(r"../../Downloads/Female_jeans.jfif", 'rb') as file:
            image = SimpleUploadedFile(name='Female_jeans.jfif', content=file.read(), content_type='image/jpeg')

        Product.objects.create(product_name='Test Product 1', product_category='Test Category 1', product_image=image)
        Product.objects.create(product_name='Test Product 2', product_category='Test Category 2', product_image=image)

    def test_home_view(self):
        response = self.client.get(self.home_url)
        allProds = response.context['allProds']

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(allProds), 2)

        # Check that 'Test Product 1' and 'Test Product 2' are in allProds, regardless of their order
        product_names = [prod[0][0].product_name for prod in allProds]
        self.assertIn('Test Product 1', product_names)
        self.assertIn('Test Product 2', product_names)