from django.test import TestCase
from django.contrib.auth import get_user_model


class AuthTest(TestCase):
    '''Тестирование аутентификации пользователя'''
    def setUp(self):
        get_user_model().objects.create_user(username='admin', password='12345678')


    def test_auth_pages(self) -> None:
        login = self.client.get('/users/login/')
        self.assertEqual(login.status_code, 200)

        register = self.client.get('/users/register/')
        self.assertEqual(register.status_code, 200)

        logout = self.client.get('/users/logout/')
        self.assertEqual(logout.status_code, 302)
    
    
    def test_register(self):
        username = 'user'
        response = self.client.post('/users/register/', {
            'username': username,
            'email': 'user@test.com',
            'first_name': 'user_name',
            'last_name': 'user_lastname',
            'password1': '12345678',
            'password2': '12345678',
        })
        user = get_user_model().objects.get(username=username)
        self.assertEqual(user.is_authenticated, True)


    def test_login(self) -> None:
        ans = self.client.login(username='admin', password='12345678')
        self.assertEqual(ans, True)

