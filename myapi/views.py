from rest_framework import viewsets
from django.contrib.auth.models import User
from myapi.models import Hero
from .serializers import UserSerializer,HeroSerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer    