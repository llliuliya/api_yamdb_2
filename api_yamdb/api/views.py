from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.shortcuts import get_object_or_404

from api.permissions import IsOwnerOrReadOnly
from api.serializers import CommentSerializer, ReviewSerializer

from reviews.models import Comment, Title, Review
from users.models import User


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        queryset = Review.objects.filter(title=title_id)
        return queryset

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        queryset = Comment.objects.filter(review=review_id)
        return queryset

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)
