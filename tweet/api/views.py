from rest_framework import generics
from tweet.models import Tweet
from .pagination import StandardResultPagination
from .serializer import TweetModelSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class LikeToggleView(APIView):
    def get(self, request, pk, format=None):
        tweet_qs = Tweet.objects.filter(pk=pk)
        message = 'Not Allowed'
        if request.user.is_authenticated:
            is_liked = Tweet.objects.like_toggle(
                request.user, tweet_qs.first())
            return Response({"liked": is_liked})
        return Response({"message": message}, status=400)


class TweetListAPIView(generics.ListAPIView):
    pagination_class = StandardResultPagination
    serializer_class = TweetModelSerializer

    def get_queryset(self):
        return Tweet.objects.all()
