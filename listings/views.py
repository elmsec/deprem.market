from rest_framework import viewsets, permissions

from deprem.permissions import IsSuperUserOrReadOnly

from .models import Listing, Category
from .serializers import ListingSerializer, CategorySerializer


class ListingViewSet(viewsets.ModelViewSet):
    queryset = Listing.objects.all()
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        queryset = Listing.objects.all()
        listing_type = self.request.query_params.get('listing_type', None)
        category = self.request.query_params.get('category', None)
        if listing_type is not None:
            queryset = queryset.filter(listing_type=listing_type)

        if category is not None:
            queryset = queryset.filter(category=category)

        return queryset


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsSuperUserOrReadOnly,)
