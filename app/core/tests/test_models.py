from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email='test@test.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


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

    def test_new_user_invalid_username(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@test.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_can_str(self):
        """Test the can string representation"""
        can = models.Can.objects.create(
            user=sample_user(),
            title='Baked Beans',
            quantity=5
        )

        self.assertEqual(str(can), can.title)
