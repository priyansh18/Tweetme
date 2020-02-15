from rest_framework import generics
from tweet.models import Tweet
from .pagination import StandardResultPagination
from .serializer import TweetModelSerializer

class TweetListAPIView(generics.ListAPIView):
    pagination_class = StandardResultPagination
    serializer_class = TweetModelSerializer
    def get_queryset(self):
        return Tweet.objects.all()