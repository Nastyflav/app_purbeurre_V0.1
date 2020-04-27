#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-24
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase, Client, TransactionTestCase
from django.db import IntegrityError
from django.urls import reverse
from .models import Category, Product
from authentication.models import User
from django.core.management import call_command
from unittest.mock import patch


def db_init():
    """ setUp Test """
    user = User.objects.create(email='remy@purbeurre.fr')
    user.set_password('pixar20')
    user.save()

    data = Category(name="Epices")
    data.save()

    data = Product(
        name="Coriandre",
        description="De la coriandre congelée pour agrémenter vos plats"
        category_id=Category.objects.get(name="Epices"),
        store="Carrefour"
        nutriscore="c",
        barcode="012456870000"
        url="https://coriandre.fr",
        photo="https://coriandre.fr/photo.jpg",
        lipids_for_100g="2.60"
        saturated_fats_for_100g="0.59"
        sugars_for_100g="0.11"
        salt_for_100g="3.51"
    )
    data.save()

    data = Product(
        name="Garam masala",
        description="Une épice indienne qui vient des rives du Gange"
        category_id=Category.objects.get(name="Epices"),
        store="Leclerc, BioCoop"
        nutriscore="a",
        barcode="0189654870000"
        url="https://garam-masala.fr",
        photo="https://garam-masala.fr/photo.jpg",
        lipids_for_100g="4.59"
        saturated_fats_for_100g="0.02"
        sugars_for_100g="1.54"
        salt_for_100g="3.25"
    )
    data.save()

    data = Product(
        name="Paprika",
        description="Très utilisé en cuisine sud-américaine"
        category_id=Category.objects.get(name="Epices"),
        store="Auchan"
        nutriscore="b",
        barcode="012232370000"
        url="https://paprika.fr",
        photo="https://paprika.fr/photo.jpg",
        lipids_for_100g="1.64"
        saturated_fats_for_100g="0.33"
        sugars_for_100g="2.20"
        salt_for_100g="1.06"
    )
    data.save()

