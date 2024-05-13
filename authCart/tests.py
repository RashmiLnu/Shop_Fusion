from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages

class SignUpTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signUp')  # replace 'signup' with the actual name of the signUp view in your urls.py

    def test_signup_success(self):
        response = self.client.post(self.signup_url, {
            'email': 'test@example.com',
            'pass1': 'testpassword',
            'pass2': 'testpassword'
        })

        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='test@example.com').exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Account created successfully')

    def test_signup_passwords_do_not_match(self):
        response = self.client.post(self.signup_url, {
            'email': 'test@example.com',
            'pass1': 'testpassword',
            'pass2': 'differentpassword'
        })

        self.assertEqual(response.status_code, 200)
        self.assertFalse(User.objects.filter(username='test@example.com').exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Passwords do not match')

    def test_signup_email_already_exists(self):
        User.objects.create_user('test@example.com', 'test@example.com', 'testpassword')

        response = self.client.post(self.signup_url, {
            'email': 'test@example.com',
            'pass1': 'testpassword',
            'pass2': 'testpassword'
        })

        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'A user with this email already exists.')
