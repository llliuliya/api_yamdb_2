from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import CommentViewSet, ViewSet

router = DefaultRouter()
router.register(r'review', ViewSet, basename='review')
router.register(r'comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
]
