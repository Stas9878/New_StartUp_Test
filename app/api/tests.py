from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import force_authenticate
from rest_framework.test import APIRequestFactory
from .views import LinkAPIView, DecodeLinkAPIView
from links.models import Links



class APITest(TestCase):
    '''Тестирование API'''
    def setUp(self) -> None:
        user = get_user_model().objects.create_user(username='admin', password='12345678')
        link1 = Links.objects.create(
            code = 'qwertyui',
            old_url = 'https://example.com/apiv1/test1',
            new_url = 'example.com/qwertyui',
            user = user,
        )
        

    def test_create_link(self) -> None:
        header = {'url': 'https://example.com/apiv1/test3'}
        response = self.client.post('/api/v1/create-link/', headers=header)
        queryset = Links.objects.all()

        self.assertEqual(len(queryset), 2)
        self.assertEqual(len(queryset[1].code), 8)
        self.assertEqual(queryset[1].old_url, header['url'])
    

    def test_user_links(self) -> None:
        factory = APIRequestFactory()
        user = get_user_model().objects.get(username='admin')
        view = LinkAPIView.as_view()

        request = factory.get('/api/v1/api-auth/login/')
        force_authenticate(request, user=user)
        
        response = view(request)
        link = Links.objects.get(user=user).new_url
        new_url = response.data['links'][0]['new_url']

        self.assertEqual(new_url, link)
    
    
    def test_decode_url(self) -> None:
        factory = APIRequestFactory()
        user = get_user_model().objects.get(username='admin')
        view = DecodeLinkAPIView.as_view()

        request = factory.post('/api/v1/decode-url/', headers={'url': 'example.com/qwertyui'})
        response = view(request)

        link = Links.objects.get(user=user).old_url
        old_url = response.data['old_url']

        self.assertEqual(old_url, link)

        