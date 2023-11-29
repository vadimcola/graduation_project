from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


# TODO Здесь нам придется переопределить сериалайзер, который использует djoser
# TODO для создания пользователя из за того, что у нас имеются нестандартные поля


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'phone', 'image')

    def create(self, validated_data):
        new_user = User.objects.create_user(**validated_data)
        if new_user.role == "admin":
            new_user.is_staff = True
            new_user.save()
            return new_user
        return new_user


class CurrentUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'phone', 'id', 'email', 'image')
