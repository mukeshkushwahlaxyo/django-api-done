"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .routers import router
from rest_framework_simplejwt import views as jwt_views 

urlpatterns = [
 # path('api/', include(router.urls)),
 	path('', include('myapi.urls')),
 	path('rest-auth/', include('rest_auth.urls')),
 	path('accounts/', include('rest_registration.api.urls')),
  	path('api/login/',jwt_views.TokenObtainPairView.as_view(),name ='token_obtain_pair'), 
    path('api/token/refresh/',jwt_views.TokenRefreshView.as_view(),name ='token_refresh'),    
]
