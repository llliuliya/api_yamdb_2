from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import (RegexValidator,
                                    MaxValueValidator,
                                    MinValueValidator)

User = get_user_model()


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.TextField(null=True)
    genre = models.ManyToManyField(
        'Genre',
        through='GenreTitle',
        related_name='title_genre'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='title_category'
    )

    def __str__(self):
        return self.name


class GenreTitle(models.Model):
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name='genre_title'
    )
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category} {self.title}'


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(
        max_length=50,
        unique=True,
        validators=[RegexValidator(
            regex=r'^[-a-zA-Z0-9_]+$',
            message='Слаг должен состоять из строчных и заглавных '
                    'латинских букв, цифр, дефиса или нижнего подчеркивания'
        )]
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    score = models.IntegerField(validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.text, self.score


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.text
