from django.test import TestCase

class LinksTest(TestCase):
    '''Тестирование приложения links'''


    def test_link_page(self) -> None:
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Главная')
        self.assertContains(response, 'API')
    
    
    def test_short_url(self):
        response = self.client.post('/', data={
            'target_url': 'https://example.com/example/lesson/api/1'
        })
        self.assertContains(response, 'Результат:')
        print(response.content.decode())


