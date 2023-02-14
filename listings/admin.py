from django.contrib import admin
from .models import Category, Listing


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'created_at', 'updated_at')
    list_filter = ('is_active', 'created_at', 'updated_at')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'listing_type', 'created_by', 'created_at', 'updated_at')
    list_filter = ('listing_type', 'created_by', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'offer')
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('category', 'created_by')
