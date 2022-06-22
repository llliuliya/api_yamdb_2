from rest_framework.routers import DefaultRouter

from django.urls import include, path

from api.views import CommentViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'review', ReviewViewSet, basename='review')
router.register(r'comments', CommentViewSet, basename='comments')


urlpatterns = [
    path('v1/', include(router.urls)),
]
