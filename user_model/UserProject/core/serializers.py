from rest_framework.serializers import ModelSerializer, ListSerializer
from django.contrib.auth.models import User
from core.models import Car, Students

from rest_framework.authtoken.models import Token 

class UserModelSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ('username', 'password', 'email', 'id') 
        extra_kwargs = {'password': {'write_only':True}}

class CarModelSerializer(ModelSerializer):
    class Meta:
        model = Car 
        fields = '__all__' 

class StudentModelSerializer(ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__' 

class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ('username', 'password', 'email') 
        extra_kwargs = {'password': 
            {'write_only': True},
        }
    
    def create(self, data):
        user = User(email=data['email'],username=data['username'])
        user.set_password(data['password']) 
        user.save() 
        Token.objects.create(user=user) 
        return user 
        