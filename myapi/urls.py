
from rest_framework import routers
from . import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'heroes', views.ArticleViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('get_user', views.ArticleViewSet.current_user ,name='getUser'),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]