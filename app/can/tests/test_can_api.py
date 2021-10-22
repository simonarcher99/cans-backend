from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import serializers, status

from can.serializers import CanSerializer

import os

from core.models import Can


CAN_URL = reverse('can:can')


def delete_edit_can_url(pk):
    return os.path.join(reverse('can:can') + f'{pk}')


def create_can(user, **kwargs):
    """Helper function to create a can object"""
    defaults = {
        'title': 'baked beans',
        'quantity': 5
    }
    defaults.update(kwargs)

    return Can.objects.create(user=user, **defaults)


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

        res = self.client.post(CAN_URL, payload)
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

        res = self.client.post(CAN_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        exists = Can.objects.filter(
            user=self.user,
            title=payload['title']
        ).exists()
        self.assertTrue(exists)

    def test_list_logged_in_users_cans(self):
        """Test that the cans listed are the ones belonging to the currently authenticated user"""
        payload = {
            'title': 'baked beans',
            'quantity': 5
        }

        user2 = get_user_model().objects.create_user(
            email='test2@test.com',
            password='password1232'
        )
        Can.objects.create(user=user2, title='chick peas', quantity=5)
        Can.objects.create(user=self.user, **payload)

        res = self.client.get(CAN_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

    def test_list_cans_returns_all_cans(self):
        """Test that the list cans endpoint returns all the users cans"""
        create_can(user=self.user)
        create_can(user=self.user, title='mango chutney', quantity=5)

        res = self.client.get(CAN_URL)

        cans = Can.objects.filter(user=self.user)
        serializer = CanSerializer(cans, many=True)
        self.assertEqual(len(res.data), 2)
        self.assertEqual(res.data, serializer.data)

    def test_delete_can(self):
        """Test that if a user deletes a can it is removed from the database"""
        can = create_can(user=self.user)

        url = delete_edit_can_url(can.id)
        res = self.client.delete(url)

        cans = Can.objects.all()
        self.assertEqual(len(cans), 0)
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

    def test_patch_can(self):
        """Test that the user can edit the quantity of the can"""
        can = create_can(user=self.user)
        quantity = can.quantity

        url = delete_edit_can_url(can.id)
        payload = {
            'quantity': quantity - 1
        }
        res = self.client.patch(url, payload)

        can_edited = Can.objects.filter(id=can.id)[0]
        serializer = CanSerializer(can_edited)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(serializer.data['quantity'], quantity-1)
