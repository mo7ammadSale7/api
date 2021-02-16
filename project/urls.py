# from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth import get_user_model
from rest_framework import routers, viewsets, serializers

from board.views import ListViewSet, CardViewSet, CommentViewSet

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('lists', ListViewSet)
router.register('cards', CardViewSet)
router.register('comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls)
]