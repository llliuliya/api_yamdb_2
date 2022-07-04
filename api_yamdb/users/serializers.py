from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import serializers

User = get_user_model()

FIELDS = (
    'username',
    'email',
    'first_name',
    'last_name',
    'bio',
    'role'
)


# TODO: Нужен сериалайзер, для Модели. Чтобы в нем создать пользователя.
# Для почты используй EmailField - в нем уже есть валидация почты.
class UserSignUpSerializer(serializers.ModelSerializer):
    """Создание пользователя, отправка на почту кода."""
    ...

    class Meta:
        model = User
        fields = ('username', 'email')

    # TODO: Добавить валидацию на проверку уникальности username и email
    # Запрет использование username == 'me'
    def validate(self, data):
        ...
        return data


# TODO: Создать отдельный сериалайзер для проверки переданных данных.
class UserTokenSerializer(serializers.Serializer):
    """Получение токена."""
    ...

    class Meta:
        ...

    # TODO: Добавить валидацию, чтобы проверить код.
    # Получить пользователя с помощью get_object_or_404. Чтобы, если нет
    # юзера с переданными username, то вернуть 404.
    def validate(self, attrs):
        ...
        return attrs


class UserSerializer(serializers.ModelSerializer):
    """ Получение кода подтверждения для регистрации пользователя. """
    class Meta:
        model = User
        fields = FIELDS

    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError("выберите другое имя")
        return value


class UserSelfSerializer(UserSerializer):
    """ Создание пользователя. """
    class Meta:
        model = User
        fields = FIELDS
        read_only_fields = ('role',)
