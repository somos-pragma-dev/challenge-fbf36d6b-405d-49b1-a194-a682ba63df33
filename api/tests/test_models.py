from django.test import TestCase
from..models import Product

class ProductModelTest(TestCase):
    def test_product_creation(self):
        product = Product.objects.create(name='Test Product', price=10.00, stock=100, category='Test Category')
        self.assertEqual(product.name, 'Test Product')