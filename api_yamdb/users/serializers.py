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


# Нужне сериалайзер, для Модели. Чтобы в нем создать пользователя.
class UserSignUpSerializer(serializers.ModelSerializer):
    """Создание пользователя, отправка на почту кода."""
    username = serializers.CharField()
    # EmailField - в нем уже валидация почты.
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email')

    # TODO: Добавить валидацию на проверку уникальности username и email
    # Запрет использование username == 'me'
    def validate(self, data):
        email, username = data['email'], data['username']
        if username == 'me':
            raise serializers.ValidationError("Нельзя использовать имя ME")

        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError("Должно быть уникальынм.")

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError("Должно быть уникальынм.")

        return data


# Создать отдельный сериалайзер для проверки переданных данных.
class UserTokenSerializer(serializers.Serializer):
    """Получение токена."""
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        fields = ('username', 'confirmation_code')

    # TODO: Добавить валидацию, чтобы проверить код.
    # Получить пользователя с помощью get_object_or_404. Чтобы, если нет
    # юзера с переданными username, то вернуть 404.
    def validate(self, attrs):
        user = get_object_or_404(User, username=attrs.get('username'))
        if user.confirmation_code != attrs.get('confirmation_code'):
            raise serializers.ValidationError("Неверный код.")
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
