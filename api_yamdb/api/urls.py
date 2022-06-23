from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, GenreViewSet, TitleViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'category', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router.urls))
]
