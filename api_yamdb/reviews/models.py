from django.db import models
from django.core.validators import (RegexValidator,
                                    MaxValueValidator,
                                    MinValueValidator)

from users.models import User


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
    genre = models.ForeignKey(
        'Genre',
        on_delete=models.CASCADE,
        related_name='genre'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='title')

    def __str__(self):
        return f'{self.genre} {self.title}'


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(
        max_length=50,
        unique=True
    )

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
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    score = models.IntegerField(validators=[
        MaxValueValidator(10),
        MinValueValidator(1)
    ])
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['title', 'author'],
                name='unique_review')
        ]

    def __str__(self):
        return f'{self.text}, {self.score}'


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return self.text
