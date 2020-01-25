from django.test import TestCase
from .functions import previous_years, get_products_for_carousel
from products.models import Product


class TestHelperFunctions(TestCase):

    def test_previous_years(self):
        """testing function returning a list with range from previous year to current
        as user can input only int is only tested against int (delta)"""
        delta = 10
        current_year = 2020
        result = previous_years(delta)
        self.assertEqual(result[0], current_year-delta-1)
        self.assertEqual(result[0], 2009)

    def setUp(self):
        """filling test db with dummy products"""
        Product.objects.create(
            name='testname', description='test description', offer=10, price=20, category="", stock=3)
        Product.objects.create(
            name='testname2', description='test description', offer=5, price=30, category="", stock=3)
        Product.objects.create(
            name='testname3', description='test description', offer=0, price=30, category="", stock=3)

    def test_get_products_for_carousel(self):
        """testing function that returns list of products 
        with offer and ordered from grater discount to lesser"""
        products = Product.objects.all()
        result = get_products_for_carousel(products)
        self.assertTrue(len(result), 2)
        self.assertGreater(result[0].discount,result[1].discount)

