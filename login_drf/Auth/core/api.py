from rest_framework.generics import CreateAPIView 
from django.contrib.auth.models import User 
from core.serializers import UserSerializer 
from rest_framework.views import APIView 
from django.contrib.auth import authenticate 
from rest_framework.response import Response 
from rest_framework import status 
from rest_framework.authtoken.models import Token 
from rest_framework.viewsets import ModelViewSet 
from django.contrib.auth.models import User 
from core.serializers import UserModelSerializer


class UserCreateViewSet(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    fields = ('username', 'password', 'email') 
    permission_classes = ()
    authentication_classes = () 

class LoginAPIView(APIView):
    permission_classes = () 
    authentication_classes = () 

    def post(self, request):
        username = request.data.get('username') 
        password = request.data.get('password') 
        user = authenticate(username = username, password = password) 

        if user:
            return Response({'token': user.auth_token.key}) 
        else:
            return Response({'error': 'Wrong Crendentials!!'}, status.HTTP_400_BAD_REQUEST)

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserModelSerializer 
    fields = ('username', 'password', 'email') 
    allowed_methods = ('GET', 'POST', 'HEAD', 'OPTIONS', 'DELETE', 'UPDATE', 'PUT') 
    authentication_classes = ()
    permission_classes = () 



