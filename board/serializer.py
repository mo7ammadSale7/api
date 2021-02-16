from rest_framework import serializers

from .models import List, Card, Comment

class ListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = List
        fields = ['url', 'pk', 'title', 'member', 'cards']


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'pk', 'body', 'created_date', 'user', 'card', 'parent', 'replies']


class CardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Card
        fields = ['url', 'pk', 'title', 'description', 'author', 'list', 'comments']


