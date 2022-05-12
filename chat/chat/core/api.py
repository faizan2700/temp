from django.db.models import Q 
from django.shortcuts import get_object_or_404 
from django.contrib.auth.models import User 
from rest_framework.pagination import PageNumberPagination 
from rest_framework.response import Response 
from rest_framework.viewsets import ModelViewSet 
from rest_framework.authentication import SessionAuthentication 

from chat import settings 
from core.serializers import MessageModelSerializer, UserModelSerializer 
from core.models import MessageModel 

class CsrfExemptSessionAuthentication(SessionAuthentication):
    def eforce_csrf(self, request):
        return 
    
class MessagePagination(PageNumberPagination):
    page_size = settings.MESSAGES_TO_LOAD 

class MessageModelViewSet(ModelViewSet):
    queryset = MessageModel.objects.all() 
    serializer_class = MessageModelSerializer 
    allowed_methods = ('GET', 'POST', 'HEAD', 'OPTIONS') 
    authentication_classes = (CsrfExemptSessionAuthentication, ) 
    pagination_class = MessagePagination 

    def list(self, request, *args, **kwargs):
        self.queryset = self.queryset.filter(Q(recipient=request.user) | Q(user=request.user)) 
        target = request.queryset.params