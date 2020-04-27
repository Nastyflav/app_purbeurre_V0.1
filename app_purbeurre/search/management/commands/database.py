#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-27
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from ...models import Category, Product
from .constants import API_CATEGORIES, API_PAGE_SIZE, API_PAGES_NUMBER, API_URL_SOURCE
import requests as rq


class Database():
    """
    Inserts into the database the categories and all the product keys it requires
    
    """
    def add_categories(self):
        """inserts the defined categories in database"""
        for category in API_CATEGORIES:
            Category.objects.create(name=category)  

    def add_products(self):
        """inserts products of every category into the database"""
        for category in API_CATEGORIES:
            pages = API_PAGES_NUMBER
            for page in range(pages):
                payload = {'action': 'process', 'tagtype_0': 'categories', 'tag_contains_0': 'contains',  \
                        'tag_0': category, 'page_size': API_PAGE_SIZE, 'page': page,  'json': 1}
                request = rq.get(API_URL_SOURCE, params=payload)
                datas = request.json()

                for data in datas['products']:
                    products = {}
                    