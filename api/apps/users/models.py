# from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.utils.translation import gettext_lazy as _

from main.models import BaseModel


class User(AbstractUser, BaseModel):
    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['username']

    # def __str__(self):
    #     return self.email

    # Make the API accessible for everyone without email verification
    # Rate limiting is done in the view
    pass
