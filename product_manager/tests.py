from django.test import TestCase
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import reverse
from products.models import Product


class TestUserProducts(TestCase):
    def setUp(self):
        """pre setting database and user logged in"""
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        Product.objects.create(
            name='testname',
            description='test description',
            offer=10,
            price=20,
            category="",
            stock=3,
            vendor=User.objects.get(username="test"))
        Product.objects.create(
            name='testname2',
            description='test description',
            offer=10,
            price=20,
            category="",
            stock=3)

    def test_get_vendor_products(self):
        """test only products by logged in user are visible"""
        self.client.login(username='test', password='testpassword')
        response = self.client.get(reverse('user_products'))
        product_names = [x.name for x in response.context["products"]]
        self.assertIn('testname', product_names)
        self.assertNotIn('testname2', product_names)
        self.assertTemplateUsed('user_products.html')
