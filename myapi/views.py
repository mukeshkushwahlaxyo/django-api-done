from rest_framework import viewsets
from django.contrib.auth.models import User
from myapi.models import Hero
from .serializers import UserSerializer,HeroSerializer
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
import json
from django.http import JsonResponse
from django.core import serializers


@action(detail=False, methods=['get'])
@permission_classes((IsAuthenticated,))
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def current_user(request):
    	user_id = request.user.id
    	queryset = User.objects.filter(id = request.user.id)
    	serializer_class = UserSerializer(queryset, many = True)
    	# return user_serializer
    	return JsonResponse(serializer_class,safe=False)

class HeroViewSet(viewsets.ModelViewSet):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer    