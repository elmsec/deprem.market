from rest_framework import serializers

from listings.models import Listing, Category


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'url',
            'id',
            'title',
            'slug',
            'description',
            'listing_type',
            'category',
            'created_by',
            'created_at',
            'updated_at',
        ]


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = [
            'url',
            'id',
            'name',
            'slug',
            'is_active',
            'created_at',
            'updated_at',
        ]
