from django.contrib.auth.models import User, Group
from rest_framework import viewsets
# from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from quickstart.serializers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    用户API节点
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    组API节点
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer