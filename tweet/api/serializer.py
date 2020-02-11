from rest_framework import serializers

from tweet.models import Tweet
from accounts.api.serializer import UserDispalySerializer

class TweetModelSerializer(serializers.ModelSerializer):
    user = UserDispalySerializer()
    class Meta:
        model = Tweet
        fields = [
            'user','content'
        ]