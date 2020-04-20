from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    """Model to create a user, based on an email authentication"""
    email = models.EmailField(unique=True, null=True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, blank=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'    #send the user email as a user name to the authentication form