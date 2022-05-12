from rest_framework.viewsets import ModelViewSet 
from core.serializers import UserSerializer 
from django.contrib.auth.models import User 
from rest_framework.views import APIView 
from django.contrib.auth import authenticate 
from rest_framework.response import Response 
from rest_framework.status import HTTP_400_BAD_REQUEST as bad_request

class UserViewSet(ModelViewSet):
    queryset = User.objects.all() 
    serializer_class = UserSerializer 
    permission_classes = () 
    authentication_classes = () 
    fields = ('username', 'password', 'email') 
    allowed_methods = ('GET', 'POST', 'OPTIONS', 'HEAD', 'DELETE')

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
            return Response({'error': 'Wrong Credentials'}, status=bad_request) 
