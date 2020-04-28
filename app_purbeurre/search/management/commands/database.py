#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-27
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.db import IntegrityError
from decimal import Decimal, DecimalException
from ...models import Category, Product
from .constants import API_CATEGORIES, API_PAGE_SIZE, API_PAGES_NUMBER, API_URL_SOURCE, REQUIRED_KEYS
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

                for product in datas["products"]:
                    if not Product.objects.filter(
                        barcode=product["code"]
                    ).exists():  # avoiding KeyError, duplicates
                        try:
                            Product.objects.create(
                                name=product.get('product_name_fr'),
                             
                                category_id=Category.objects.get(
                                    name=category
                                ),
                                store=product.get('stores'),
                                nutriscore=product.get('nutrition_grade'),
                                barcode=product.get('code', None),
                                url=product.get('url'),
                                image=product.get('image_url'),
                                # nutriments
                            
                                lipids_for_100g=product["nutriments"].get(
                                    "fat_100g"
                                ),
                                saturated_fats_for_100g=product["nutriments"].get(
                                    "saturated-fat_100g"
                                ),
                                 sugars_for_100g=product["nutriments"].get(
                                    "sugars_100g"
                                ),
                                salt_for_100g=product["nutriments"].get(
                                    "salt_100g"
                                ),
        
                               
                            )
                        except (IntegrityError, DecimalException):
                            pass
                    else:
                        Product.objects.filter(
                            barcode=product.get("code", None)).update(
                            name=product.get("product_name_fr"),
                      
                            category_id=Category.objects.get(
                                name=category
                            ),
                            store=product.get('stores'),
                            nutriscore=product.get("nutriscore_grade"),
                            image=product.get("image_url"),
                            url=product.get("url"),
                            # nutriments
                        
                            lipids_for_100g=product["nutriments"].get(
                                "fat_100g"
                            ),
                            saturated_fats_for_100g=product["nutriments"].get(
                                "saturated-fat_100g"
                            ),
                            sugars_for_100g=product["nutriments"].get(
                                "sugars_100g"
                            ),
                            salt_for_100g=product["nutriments"].get(
                                "salt_100g"
                            )
                            
                        )

                # for data in datas['products']:
                #     product = {}
                #     for key in REQUIRED_KEYS:
                #         product[key] = data.get(key)
                #     if all(product.values()):
                #         nutriments = data.get('nutriments')
                #         prod = Product(
                #             name=product.get('product_name_fr'),
                #             generic_name_fr=product.get('generic_name_fr'),
                #             stores=product.get('stores'),
                #             nutrition_grade=product.get('nutrition_grade_fr'),
                #             code=product.get('code'),
                #             url=product.get('url'),
                #             image_url=product.get('image_url'),
                #             lipids_for_100g=nutriments.get('fat_100g'),
                #             saturated_fat_for_100g=nutriments.get('saturated-fat_100g'),
                #             sugars_for_100g=nutriments.get('sugars_100g'),
                #             salt_for_100g=nutriments.get('salt_100g')
                #         )
                #         prod.save()
                
                #         categories = data.get('categories')
                #         cat_list = categories.split(",")
                #         for category in cat_list:
                #             category = category.strip()
                #             if category in API_CATEGORIES:
                #                 category = Category.objects.get(name=category)
                #                 prod.category.add(category)

