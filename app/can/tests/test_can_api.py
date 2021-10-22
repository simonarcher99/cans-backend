from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

from can.serializers import CanSerializer

from core.models import Can


CREATE_CAN_URL = reverse('can:can')


class TestPublicCanApi(TestCase):
    """Test the public api for cans"""

    def setUp(self):
        """Setup for the tests"""
        self.client = APIClient()

    def test_create_can_not_authenticated(self):
        """Test that an unauthenticated user cannot create can"""
        payload = {
            'title': 'Baked beans',
            'quantity': 5
        }

        res = self.client.post(CREATE_CAN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class TestPrivateCanApi(TestCase):
    """Test the private can API"""

    def setUp(self):
        """Setup for the tests"""
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='pass123'
        )
        self.client.force_authenticate(user=self.user)

    def test_create_can(self):
        """Test that an authenticated user can create can"""
        payload = {
            'title': 'Baked beans',
            'quantity': 5
        }

        res = self.client.post(CREATE_CAN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        exists = Can.objects.filter(
            user=self.user,
            title=payload['title']
        ).exists()
        self.assertTrue(exists)
