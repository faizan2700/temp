from rest_framework.serializers import ModelSerializer 
from filter_app.models import Product, Manufacturer

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__' 

class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer 
        fields = '__all__' 
    