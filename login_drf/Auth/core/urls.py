from django.urls import path, include 
from rest_framework.routers import DefaultRouter 

from core.api import  UserCreateViewSet 
from core.api import UserModelViewSet
from core.api import LoginAPIView 

router = DefaultRouter() 
router.register(r'user', UserModelViewSet)

urlpatterns = [
    path(r'users', UserCreateViewSet.as_view()), 
    path('api/', include(router.urls)), 
    path('login/', LoginAPIView.as_view())
]