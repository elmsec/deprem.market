from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model


from main.models import BaseModel


User = get_user_model()


class Category(BaseModel):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class Listing(BaseModel):
    LISTING_TYPE = (
        ('offer', _('Offer')),
        ('request', _('Request')),
    )
    OFFER_TYPE = (
        ('job', _('Job')),
        ('service', _('Service')),
        ('product', _('Product')),
        ('financial_support', _('Financial Support')),
    )

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField()
    listing_type = models.CharField(max_length=50, choices=LISTING_TYPE)
    offer_type = models.CharField(max_length=50, choices=OFFER_TYPE)
    category = models.ForeignKey(
        Category,
        related_name='listings',
        on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        User,
        related_name='listings',
        on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = _('Listing')
        verbose_name_plural = _('Listings')

    def __str__(self):
        return self.title
