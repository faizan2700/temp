from rest_framework.serializers import ModelSerializer 
from django.contrib.auth.models import User 
from rest_framework.authtoken.models import Token 


class UserSerializer(ModelSerializer):
    class Meta:
        model = User 
        fields = ('username', 'password', 'email') 
        extra_kwargs = {'password': {'write_only': True}} 
    
    def create(self, data):
        username = data['username'] 
        email = data['email'] 
        password = data['password']
        user = User(username = username, email = email) 
        user.set_password(password) 
        user.save() 
        Token.objects.create(user=user) 
        return user 
