from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [  # TODO: check fields for security
            'url',
            'id',
            'username',
            'first_name',
            'last_name',
            'is_staff',
            'is_active',
            'date_joined',
            'last_login',
            'password',
            'confirm_password',
        ]
        extra_kwargs = {
            'is_staff': {'read_only': True},
            'is_active': {'read_only': True},
            'date_joined': {'read_only': True},
            'last_login': {'read_only': True},
            'password': {'write_only': True},
            'first_name': {'required': False},
            'last_name': {'required': False},
        }


class UserCreateSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password',
            'confirm_password',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': False, 'allow_blank': True},
            'last_name': {'required': False, 'allow_blank': True},
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
        )
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']
        if password != confirm_password:
            raise serializers.ValidationError(
                {'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
