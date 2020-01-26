from django.test import TestCase
from .models import Product


class TestProductModel(TestCase):
    def setUp(self):
        """pre setting database"""
        Product.objects.create(name='testname',
                               description='test description',
                               offer=10,
                               price=20,
                               category="",
                               stock=3)

    def test_product_create(self):
        """test create new product"""
        product = Product.objects.get(name="testname")
        self.assertEqual('test description', product.description)
        self.assertEqual(10, product.offer)
        self.assertEqual(20, product.price)
        self.assertEqual("", product.category)
        self.assertEqual(3, product.stock)

    def test_product_pre_save_adds_disocunt(self):
        """test pre save functionality, expecting to add discount to product"""
        product = Product.objects.get(name="testname")
        self.assertEqual(18, product.discount)
