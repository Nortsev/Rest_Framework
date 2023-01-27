from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
# Create your views here.

from .serializers import UsersModelSerializer
from .models import Users


class UserModelViewSet(ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersModelSerializer
