
from rest_framework.viewsets import ModelViewSet 
from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveDestroyAPIView 
from rest_framework.generics import CreateAPIView 
from rest_framework.views import APIView 

from core.serializers import UserModelSerializer 
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated 
from core.models import Car, Students
from core.serializers import CarModelSerializer, StudentModelSerializer

from rest_framework import status
from django.contrib.auth import authenticate 

from rest_framework.response import Response
from core.serializers import UserSerializer

class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserModelSerializer 
    allowed_methods = ('GET', 'HEAD', 'OPTIONS', 'POST', 'DELETE')
    fields = ('username', 'password', 'email') 

class CarModelViewSet(ModelViewSet):
    queryset = Car.objects.all() 
    serializer_class = CarModelSerializer 
    allowed_methods = ('GET', 'HEAD', 'OPTIONS', 'POST', 'DELETE') 


class StudentModelViewSet(ModelViewSet):
    queryset = Students.objects.all() 
    serializer_class = StudentModelSerializer
    allowed_methods = ('GET', 'HEAD', 'OPTIONS', 'POST', 'DELETE') 


class UserListCreateViewSet(ListCreateAPIView):
    queryset = User.objects.all() 
    fields = '__all__'
    serializer_class = UserModelSerializer

class UserRetrieveDestroyViewSet(RetrieveDestroyAPIView):
    queryset = User.objects.all() 
    fields = '__all__'
    serializer_class = UserModelSerializer 

class UserCreateViewSet(CreateAPIView):
    queryset = User.objects.all() 
    fields = ('username', 'password', 'email')
    serializer_class = UserSerializer
    permission_classes = () 
    authentication_classes = () 

class LoginAPIView(APIView):
    permission_classes = () 
    authentication_classes = () 

    def post(self, request):
        username = request.data.get('username') 
        password = request.data.get('password') 
        user = authenticate(username=username, password=password) 
        if user:
            return Response({'token': user.auth_token.key})
        else:
            return Response({'error': 'Wrong Credentials!'}, status=status.HTTP_400_BAD_REQUEST)


