"""
Import required libraries for models
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom user model that extends Django's built-in `AbstractUser` model.

    This model uses email as the unique identifier for authentication instead of
    the default `username` field.
    """
    username = None
    email = models.EmailField(_('email address'), unique=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    """
    UserProfile model that stores additional information about a user.
    """
    user = models.OneToOneField(
        CustomUser,
        verbose_name='User Profile',
        related_name='profile',
        on_delete=models.CASCADE,
        unique=True
    )
    is_confirm = models.BooleanField(
        verbose_name='Confirm Email',
        default=False
    )
    first_name = models.CharField(
        max_length=24,
        verbose_name='First name',
        null=True,
        blank=True
    )
    second_name = models.CharField(
        max_length=24,
        verbose_name='Second name',
        null=True,
        blank=True
    )
    country = models.CharField(
        max_length=64,
        verbose_name='Country',
        null=True,
        blank=True
    )
    city = models.CharField(
        max_length=24,
        verbose_name='City',
        null=True,
        blank=True
    )
    street = models.CharField(
        max_length=128,
        verbose_name='Street',
        null=True,
        blank=True
    )
    phone = models.BigIntegerField(
        verbose_name='Phone',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.user}'
