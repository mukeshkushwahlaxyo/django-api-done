from rest_framework import routers
from myapi.views import ArticleViewSet,HeroViewSet

router = routers.DefaultRouter()
router.register(r'user', ArticleViewSet)
router.register(r'article', HeroViewSet)