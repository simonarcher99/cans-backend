from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a user with email"""
        email = 'test@test.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(email, password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test that the email for a new user is normalized"""
        email = "test@TEST.com"
        user = get_user_model().objects.create_user(email, 'pass123')

        self.assertEqual(user.email, email.lower())
