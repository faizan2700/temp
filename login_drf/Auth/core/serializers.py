from rest_framework.serializers import ModelSerializer 
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token

class UserSerializer(ModelSerializer):
    class Meta:
        fields = ('username', 'password', 'email') 
        model = User 
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, data):
        user = User(username = data['username'], email = data['email']) 
        user.set_password(data['password'])
        user.save() 
        Token.objects.create(user=user) 
        return user 

class UserModelSerializer(ModelSerializer):
    class Meta:
        fields = ('username', 'password', 'email') 
        model = User 
        