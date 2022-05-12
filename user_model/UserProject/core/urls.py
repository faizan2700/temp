from django.urls import path, include 
from core.api import (UserModelViewSet, 
                      CarModelViewSet,
                      StudentModelViewSet,
                      UserListCreateViewSet,
                      UserRetrieveDestroyViewSet,
                      UserCreateViewSet,
                      LoginAPIView, 
                      )
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserModelViewSet)
router.register(r'cars', CarModelViewSet)
router.register(r'students', StudentModelViewSet, basename='students')
#router.register(r'users1', UserListCreateViewSet, basename='users1')
#router.register(r'users2', UserRetrieveDestroyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users_listcreate', UserListCreateViewSet.as_view(),  name = 'users_list'), 
    path('users_retdes/<int:pk>', UserRetrieveDestroyViewSet.as_view(), name='users_retdes'),
    path('user_create', UserCreateViewSet.as_view(), name='user_create'),
    path('login/', LoginAPIView.as_view(), name='login') 
]