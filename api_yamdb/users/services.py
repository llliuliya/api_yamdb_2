from django.contrib.auth.tokens import PasswordResetTokenGenerator

GENERATOR = PasswordResetTokenGenerator()


def generate_token(user):
    """Создание токена."""
    return GENERATOR.make_token(user)


def check_token(user, token):
    """Проверка токена."""
    return GENERATOR.check_token(user, token)
