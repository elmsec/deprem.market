from django.contrib.auth import get_user_model

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import UserSerializer, UserCreateSerializer
from deprem.permissions import IsSuperUserOrCanRegisterAndViewListOnly
from rest_framework_simplejwt.tokens import RefreshToken


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrCanRegisterAndViewListOnly,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return get_user_model().objects.all()
        return get_user_model().objects.none()

    @action(
        detail=False,
        methods=['post'],
        # permission_classes=[IsSuperUserOrCanRegisterOnly]
    )
    def register(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": UserSerializer(
                user,
                context=self.get_serializer_context()
            ).data,
            "token": {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        })
