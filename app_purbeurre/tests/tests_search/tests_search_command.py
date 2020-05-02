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

from search.models import Category, Product


class TestCommand(TransactionTestCase):
    pass
