#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-30
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

from search.models import Product
from .models import Favorites


class SubstitutionView(ListView):
    """
    Displays a list of products to replace the selected one
    
    Arguments: ListView {class} -- generic listview
    
    Returns: products -- products with better nutriscore in the same category
    
    """
    model = Product
    paginate_by = 6
    template_name = 'save/substitution.html'

    def get(self, request, *args, **kwargs):
        try:
            product = Product.objects.get(pk=self.kwargs['product_id'])
            return super(SubstitutionView, self).get(request, *args, **kwargs)
        except Product.DoesNotExist:
            return redirect('index')

    def get_queryset(self):
        """Allows some products from the same category"""
        self._id = self.kwargs['product_id']
        self.product = Product.objects.get(pk=self._id)
        return Product.objects.filter(
            category_id=self.product.category_id).filter(
            nutriscore__lte=self.product.nutriscore).exclude(
            id=self._id).order_by('nutriscore')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search'] = self.product.name
        context['product'] = self.product.id
        context['image'] = self.product.image
        return context

class FavoritesView(ListView):
    pass