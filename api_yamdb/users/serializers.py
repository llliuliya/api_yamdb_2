from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()

FIELDS = (
    'username',
    'email',
    'first_name',
    'last_name',
    'bio',
    'role'
)


class UserSignUpSerializer(serializers.Serializer):
    """ Получение токена и регистрация нового пользователя. """
    username = serializers.CharField()
    confirmation_code = serializers.CharField()

    class Meta:
        fields = ('username', 'confirmation_code')


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
