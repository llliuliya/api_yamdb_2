from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import exceptions, serializers
from rest_framework.validators import UniqueTogetherValidator

from users.services import generate_token

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
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')
        validators = [
            UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=('username', 'email')
            )
        ]

    def create(self, validated_data):
        email = validated_data['email']
        username = validated_data['username']
        user = User.objects.create(
            username=username,
            email=email,
        )
        return user

        # TODO: Добавить валидацию на проверку уникальности username и email
    # Запрет использование username == 'me'
    def validate_username(self, value):
        if value == 'me':
            raise serializers.ValidationError("выберите другое имя")
        return value


# TODO: Создать отдельный сериалайзер для проверки переданных данных.
class TokenSerializer(serializers.Serializer):
    """Получение токена."""
    username = serializers.CharField(required=True)
    confirmation_code = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'confirmation_code')

    # TODO: Добавить валидацию, чтобы проверить код.
    # Получить пользователя с помощью get_object_or_404. Чтобы, если нет
    # юзера с переданными username, то вернуть 404.
    def validate(self, data):
        user = get_object_or_404(User, username=data['username'])
        if user.confirmation_code != data['confirmation_code']:
            raise exceptions.ValidationError("Код подтверждения не верный")
        return data


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
