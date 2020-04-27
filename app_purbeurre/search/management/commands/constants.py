#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-24
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

API_PAGE_SIZE = 500
API_PAGES_NUMBER = 1
API_CATEGORIES = ['Pâte à tartiner', 'Thés en sachet', 'Fromages blancs', 'Jus de fruits', 'Confitures de fruits',
                 'Céréales pour petit-déjeuner', 'Cafés', 'Pâtes alimentaires', 'Epices', 'Légumes surgelés',
                 'Sauces tomates', 'Surimi', 'Légumineuses', 'Frites', 'Galettes de céréales soufflées']
API_URL_SOURCE = 'https://fr.openfoodfacts.org/cgi/search.pl?'
REQUIRED_KEYS = KEYS = ['product_name_fr', 'generic_name_fr', 'stores', 'nutrition_grade_fr',
                        'code', 'url', 'image_url', 'fat_100g', 'saturated-fat_100g',
                        'sugars_100g', 'salt_100g']