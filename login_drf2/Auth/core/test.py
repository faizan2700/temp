from rest_framework.test import APITestCase 
from rest_framework.test import APIRequestFactory
from rest_framework.test import APIClient 

from core.api import UserViewSet

from django.contrib.auth import get_user_model 
from rest_framework.authtoken.models import Token 

class TestUser(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory() 
        self.view = UserViewSet.as_view({'get': 'list'}) 
        self.uri = '/user/' 
        self.user = self.setup_user() 
        self.token = Token.objects.create(user=self.user) 
        self.token.save() 
        self.client = APIClient() 
    
    @staticmethod 
    def setup_user():
        User = get_user_model() 
        return User.objects.create_user('test', email='testuser@test.com', password='test') 
    
    def test_list(self):
        request = self.factory.get(self.uri) 
        response = self.view(request) 
        s = 'Expected response code 200 received {} instead.'
        self.assertEqual(response.status_code, 200, s.format(response.status_code))

    
    def test_auth(self):
        request = self.factory.get(self.uri, HTTP_AUTHORIZATION='Token {}'.format(self.token.key)) 
        request.user = self.user 
        response = self.view(request) 
        s = 'Expected response code 200, received {} instead'
        self.assertEqual(response.status_code, 200, s.format(response.status_code)) 

    def test_with_client(self):
        response = self.client.get(self.uri) 
        s = 'Expected response code 200 recieved {} instead' 
        self.assertEqual(response.status_code, 200, s.format(response.status_code)) 
    
    def test_login_post(self):
        self.client.login(username='test', password='test') 
        response = self.client.post(self.uri) 
        s = 'Expected response code 200, recieved {} instead' 
        self.assertEqual(response.status_code, 201, s.format(response.status_code))  


