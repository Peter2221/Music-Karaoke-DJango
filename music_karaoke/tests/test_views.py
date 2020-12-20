from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_GET(self):
        response = self.client.get(reverse('login'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'login.html')

    def test_register_GET(self):
        response = self.client.get(reverse('register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_logout_GET(self):
        response = self.client.get(reverse('logout'))
        self.assertTrue(response.status_code in [200, 302])

    def test_landing_GET(self):
        response = self.client.get(reverse('landing'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'landing-page/landing.html')

    def test_songs_GET(self):
        response = self.client.get(reverse('songs:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'song_index.html')

    # TODO ranking GET test
    # def test_ranking_GET(self):
    #     response = self.client.get(reverse('ranking'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'register.html')

    # TODO settings GET test
    # def test_settings_GET(self):
    #     response = self.client.get(reverse('settings'))
    #     self.assertEquals(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'register.html')
