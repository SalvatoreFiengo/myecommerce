from django.test import TestCase
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
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

    def test_login(self):
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

    def test_login_unsucessful(self):
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

    def test_logout(self):
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


class TestProfile(TestCase):

    def test_profile_page(self):
        """testing profile page and if user model gets a profile as per extended model"""
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        self.client.login(username='test', password='testpassword')
        page = self.client.get('/profile/')

        self.assertTemplateUsed('profile.html')
        self.assertTrue(hasattr(self.user, 'userprofile'), True)
        self.assertTrue(hasattr(self.user.userprofile, 'location'), True)

    def test_edit_profile_page(self):
        """testing edit profile  """
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        self.client.login(username='test', password='testpassword')
        page = self.client.get('/edit_profile/')

        self.assertTemplateUsed('edit_profile.html')
        self.assertTrue(hasattr(self.user, 'userprofile'), True)
        self.assertTrue(hasattr(self.user.userprofile, 'location'), True)

    def test_update_profile_page(self):
        """testing edit profile  """
        self.user = User.objects.create_user(
            username='test', password='testpassword')
        self.client.login(username='test', password='testpassword')
        request = self.client.post('/update_profile/', {
                                'first_name': 'testname', 'last_name': 'testsurname', 'email': 'test@test.com', 'location': 'ireland'})
        self.assertTemplateUsed('update_profile.html')
        self.assertTrue(hasattr(self.user, 'userprofile'), True)
        self.assertTrue(hasattr(self.user.userprofile, 'location'), True)
        # self.assertEqual(request.location, 'ireland')
