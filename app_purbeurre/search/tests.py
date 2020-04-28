#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-24
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase, Client, TransactionTestCase
from django.db import IntegrityError
from django.urls import reverse
from django.core.management import call_command
from unittest.mock import patch

from .models import Category, Product
from authentication.models import User


def db_init():
    """Create a temp user and temp products to perform tests"""
    user = User.objects.create(email='remy@purbeurre.fr')
    user.set_password('pixar20')
    user.save()

    data = Category(name="Pate à tartiner")
    data.save()

    data = Product(
        name="Coriandre",
        description="De la coriandre congelée pour agrémenter vos plats",
        category_id=Category.objects.get(name="Pate à tartiner"),
        store="Carrefour",
        nutriscore="c",
        barcode="012456870000",
        url="https://coriandre.fr",
        image="https://coriandre.fr/photo.jpg",
        lipids_for_100g="2.60",
        saturated_fats_for_100g="0.59",
        sugars_for_100g="0.11",
        salt_for_100g="3.51",
    )
    data.save()

    data = Product(
        name="Garam masala",
        description="Une épice indienne qui vient des rives du Gange",
        category_id=Category.objects.get(name="Pate à tartiner"),
        store="Leclerc, BioCoop",
        nutriscore="a",
        barcode="0189654870000",
        url="https://garam-masala.fr",
        image="https://garam-masala.fr/photo.jpg",
        lipids_for_100g="4.59",
        saturated_fats_for_100g="0.02",
        sugars_for_100g="1.54",
        salt_for_100g="3.25",
    )
    data.save()

    data = Product(
        name="Paprika",
        description="Très utilisé en cuisine sud-américaine",
        category_id=Category.objects.get(name="Pate à tartiner"),
        store="Auchan",
        nutriscore="b",
        barcode="012232370000",
        url="https://paprika.fr",
        image="https://paprika.fr/photo.jpg",
        lipids_for_100g="1.64",
        saturated_fats_for_100g="0.33",
        sugars_for_100g="2.20",
        salt_for_100g="1.06",
    )
    data.save()


class TestSearch(TestCase):
    """To test the search app"""
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.search_url = reverse('search:search')
        cls.details_url = reverse('search:product-details')
        db_init()

    def test_search_page_returns_200(self):
        """To test the status code and the login page"""
        response = self.client.get(self.search_url +"?query=food")
        self.assertTemplateUsed(response, 'search/search_results.html')
        self.assertEqual(response.status_code, 200)

    def test_no_entry_to_search(self):
        response = self.client.get(self.search_url)
        self.assertRedirects(
            response, '/', status_code=302, target_status_code=200)


class TestCommand(TransactionTestCase):
    pass
