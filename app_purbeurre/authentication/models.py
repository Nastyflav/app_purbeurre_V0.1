#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-04-20
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    """Model to create a user, based on an email authentication"""
    email = models.EmailField(unique=True, null=True)
    firstname = models.CharField(max_length=40, blank=True)
    lastname = models.CharField(max_length=40, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'    #send the user email as a user name to the authentication form

    def __str__(self):
        return self.email
        
    class Meta:
        verbose_name = "Utilisateur"