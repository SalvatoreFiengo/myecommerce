from django.test import TestCase
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Userprofile
from .views import login


class TestAccountsView(TestCase):

    def test_get_home_page(self):
        """when surfing website url testing if home page redirects to /products/ correctly"""
        page = self.client.get('/', follow=True)
        self.assertRedirects(page,
                             "/products/",
                             status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True)

    def test_login_loads_correctly(self):
        """test login with redirect to products page and success message displayed"""
        page = self.client.get('/', follow=True)
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        response = self.client.post(
            '/login/', {'username': 'test', 'password': 'testpassword'}, follow=True)
        message = messages.get_messages(response.wsgi_request)
        self.assertTrue(self.user.is_authenticated, True)
        self.assertTrue(
            str(message), "Hi test. You are successfully logged in")
        self.assertRedirects(page,
                             "/products/",
                             status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True)

    def test_login_unsuccessful(self):
        """test login function redirects if login not successful"""
        page = self.client.get('/', follow=True)
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        response = self.client.post(
            '/login/', {'username': 'testfail', 'password': 'testpassword'})
        message = messages.get_messages(response.wsgi_request)
        self.assertTrue(self.user.is_authenticated, False)
        self.assertTrue(str(message), "your username or password is incorrect")

    def test_login_when_user_already_logged_in(self):
        """Tesing Login when user already logged in, with redirect to main page"""
        page = self.client.get('/', follow=True)
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        self.client.login(username='test', password='testpassword')
        response = self.client.post(
            '/login/', {'username': 'test', 'password': 'testpassword'})
        message = messages.get_messages(response.wsgi_request)
        self.assertTrue(str(message), " ")
        self.assertTrue(self.user.is_authenticated, True)
        self.assertRedirects(page,
                             "/products/",
                             status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True)

    def test_logout_correctly_logs_user_out(self):
        """testing logout with success message and redirect to main page"""
        page = self.client.get('/', follow=True)
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        self.client.login(username='test', password='testpassword')
        response = self.client.get('/logout/', follow=True)
        message = messages.get_messages(response.wsgi_request)
        self.assertTrue(self.user.is_authenticated, False)
        self.assertTrue(str(message), "You have successfully logged out")
        self.assertRedirects(page,
                             "/products/",
                             status_code=302,
                             target_status_code=200,
                             fetch_redirect_response=True)

    def test_registration(self):
        """test registration with success message displayed"""
        page = self.client.get('/', follow=True)
        response = self.client.post(
            '/register/', {'first_name': 'testname', 'last_name': 'testsurname', 'email': 'test@test.com'}, follow=True)
        message = messages.get_messages(response.wsgi_request)
        self.assertTrue(
            str(message), "You have successfully registered")

    def test_registration(self):
        """test registration if user already logged in redirects to index"""
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        self.client.login(username='test', password='testpassword')
        page = self.client.get('/register/', follow=True)
        message = messages.get_messages(page.wsgi_request)
        index = self.client.get('/index/', follow=True)
        self.assertTrue(
            str(message), " ")
        self.assertTemplateUsed("index.html")

    def test_registration(self):
        """test registration with success message displayed"""
        self.user = User.objects.create_user(
            username='test', password='testpassword', email='test@test.com')
        response = self.client.post(
            '/register/', {'first_name': 'testname', 'last_name': 'testsurname', 'email': 'test@test.com'}, follow=True)
        message = messages.get_messages(response.wsgi_request)
        self.assertTrue(
            str(message), "Unable to register your account at this time")

class TestUserProfileModel(TestCase):
    
    def test_create_user_with_profile(self):
        """test user adds userprofile as its extension correctly"""
        self.user = User.objects.create_user(
            username='test', password='testpassword') 
        self.assertTrue(hasattr(self.user.userprofile, 'bio'), True) 
        self.assertTrue(hasattr(self.user.userprofile, 'birth_date'), True)
        self.assertTrue(hasattr(self.user.userprofile, 'reseller'), True) 
        self.assertTrue(hasattr(self.user.userprofile, 'phone_number'), True)
        self.assertTrue(hasattr(self.user.userprofile, 'country'), True)
        self.assertTrue(hasattr(self.user.userprofile, 'post_code'), True)  
        self.assertTrue(hasattr(self.user.userprofile, 'town_or_city'), True)
        self.assertTrue(hasattr(self.user.userprofile, 'street_address1'), True)
        self.assertTrue(hasattr(self.user.userprofile, 'street_address2'), True) 
        self.assertTrue(hasattr(self.user.userprofile, 'county'), True)       

class TestProfilePage(TestCase):

    def test_profile_page(self):
        """testing profile page and if user model gets a profile as per extended model"""
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        self.client.login(username='test', password='testpassword')
        page = self.client.get('/profile/')
        self.assertTemplateUsed('profile.html')
        self.assertTrue(hasattr(self.user, 'userprofile'), True)
        self.assertTrue(hasattr(self.user.userprofile, 'phone_number'), True)

    def test_update_profile_updates_correctly(self):
        """testing edit profile """
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        self.client.login(username='test', password='testpassword')
        request = self.client.post('/update_profile/', {
                                'first_name': 'testname', 'last_name': 'testsurname', 'email': 'test@test.com', 'phone_number': '083525658'})
        self.assertTemplateUsed('update_profile.html')
        self.assertTrue(hasattr(self.user, 'userprofile'), True)
        self.assertTrue(hasattr(self.user.userprofile, 'phone_number'), True)
        self.assertTrue('083525658',self.user.userprofile.phone_number)
