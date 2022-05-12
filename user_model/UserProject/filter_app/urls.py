from django.urls import path, include 
from rest_framework.routers import DefaultRouter 
from filter_app.api import ProductViewSet, ManufacturerViewSet

router = DefaultRouter() 
router.register(r'products', ProductViewSet)
router.register(r'manufacturer', ManufacturerViewSet) 

urlpatterns = [
    path('', include(router.urls)), 
]