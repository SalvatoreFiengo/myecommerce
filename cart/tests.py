from django.test import TestCase
from django.contrib import messages
from products.models import Product


class TestAddToCart(TestCase):
    def test_view_cart_page_loads_correctly(self):
        """testing view cart page loads correctly"""
        page = self.client.get('/view_cart')
        self.assertTemplateUsed('cart.html')
    
    def test_add_to_cart_no_quantity(self):
        """testing add to cart accepts no quantity as 1"""
        product = Product({'name':'testname','description':'test description','price':20,'discount':10,'stock':3})
        product_id = product.pk
        response = self.client.post(
            '/add_to_cart/', product_id)
        quantity = response.get("quantity")
        self.assertTrue((quantity, 1),True)
    
    def test_add_to_cart_with_quantity_set(self):
        """testing add to cart accepts quantity"""
        product = Product({'name':'testname','description':'test description','price':20,'discount':10,'stock':3})
        product_id = product.pk
        response = self.client.post(
            '/add_to_cart/quantity=3', product_id)
        quantity = response.get("quantity") 
        self.assertTrue((quantity, 3),True)
    
    def test_add_to_cart_if_product_stock_is_zero(self):
        """testing add to cart returns error message if stock is 0"""
        product = Product({'name':'testname','description':'test description','price':20,'discount':10,'stock':0})
        product_id = product.pk
        response = self.client.post(
            '/add_to_cart/', product_id)
        quantity = response.get("quantity") 
        message = messages.get_messages(response.wsgi_request)
        self.assertTrue((quantity, 1),True)
        self.assertTrue(str(message), "testname, is not available at the moment")


        
