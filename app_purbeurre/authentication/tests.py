#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-21
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase, Client
from django.urls import reverse
from .models import User


class TestAuthentication(TestCase):
    """To test the authentication app"""
    def setUp(self):
        """ Create  """
        self.client = Client()
        self.login_url = reverse('authentication:login')
        self.logout_url = reverse('authentication:logout')
        self.signup_url = reverse('authentication:signup')
        self.profile_url = reverse('authentication:profile')
        self.user = User.objects.create(email='user@test.dj', firstname='John', lastname='Doe')
        self.user.set_password('supertest2020')
        self.user.save()

    def test_login_url_and_template(self):
        response = self.client.get(self.login_url)
        self.assertTemplateUsed(response, 'registration/login.html')
        self.assertEqual(response.status_code, 200)