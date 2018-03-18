from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets

from quickstart.serializers import UserSerializer, GroupSerializer


class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('date_joined')
    serializer_class = UserSerializer


class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
