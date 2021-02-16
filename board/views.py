from django.shortcuts import render
from rest_framework.permissions import BasePermission, SAFE_METHODS, IsAdminUser
from rest_framework import viewsets
from django.contrib.auth import get_user_model
from .models import List, Card, Comment
from .serializer import ListSerializer, CardSerializer, CommentSerializer

from rest_framework.pagination import PageNumberPagination

User = get_user_model()



class ListViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = List.objects.all()
    serializer_class = ListSerializer


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class ResultsSetPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = ResultsSetPagination
