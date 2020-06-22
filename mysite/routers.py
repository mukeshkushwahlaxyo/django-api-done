from rest_framework import routers
from myapi.views import ArticleViewSet

router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet)