#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-23
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.core.management.base import BaseCommand, CommandError
from .database import Database


class Command(BaseCommand):
    """Command class for custom django commands"""
    help = "Load datas from the OFF API to our database"

    def add_arguments(self, parser):
        """Set the enabled arguments for the command"""
        parser.add_argument("-c", "--category", type=str)
        parser.add_argument("-p", "--product", type=str)

    def handle(self, *args, **options):
        """Requests the API then fills the DB"""
        if not isinstance(options["category"], str):
            raise TypeError("Entrez une chaine de caractère.")

        if not isinstance(options["product"], str):
            raise TypeError("Entrez une chaine de caractère.")

        if options["category"] and options["product"]:
            self.category = options["category"]
            self.product = options["product"]


