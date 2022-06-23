from django.db.models import Avg
from rest_framework import filters, mixins, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import (CategorySerializer,
                          GenreSerializer,
                          TitleReadSerializer,
                          TitleWriteSerializer)
from .permissions import IsAdminUserOrReadOnly
from reviews.models import Category, Genre, Title


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(rating=Avg("reviews__score"))
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('category', 'genre', 'name', 'year')

    def get_serializer_class(self):
        if self.request.method in ["POST", "PATCH"]:
            return TitleWriteSerializer
        return TitleReadSerializer


class MixinSet(mixins.CreateModelMixin,
               mixins.ListModelMixin,
               mixins.DestroyModelMixin,
               viewsets.GenericViewSet):
    pass


class CategoryViewSet(MixinSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenreViewSet(MixinSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
