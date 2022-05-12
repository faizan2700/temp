from rest_framework.viewsets import ModelViewSet 
from filter_app.serializers import ProductSerializer, ManufacturerSerializer
from filter_app.models import Product, Manufacturer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer 
    authentication_classes = () 
    permission_classes = () 
    fields = '__all__'

class ManufacturerViewSet(ModelViewSet):
    queryset = Manufacturer.objects.all() 
    serializer_class = ManufacturerSerializer 
    authentication_classes = () 
    permission_classes = () 
    fileds = '__all__' 
    allowed_methods = ('GET', 'POST', 'HEAD', 'OPTIONS', 'DELETE')
    
