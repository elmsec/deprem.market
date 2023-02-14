"""
URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from users.views import UserViewSet
from listings.views import ListingViewSet, CategoryViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'listings', ListingViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path(
        'api/v1/auth/',
        include('rest_framework.urls', namespace='rest_framework'),
    ),
    path(
        'api/v1/auth/token/',
        TokenObtainPairView.as_view(),
        name='token_obtain_pair'),
    path(
        'api/v1/auth/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'),
    path(
        'api/v1/auth/token/verify/',
        TokenVerifyView.as_view(),
        name='token_verify'),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
