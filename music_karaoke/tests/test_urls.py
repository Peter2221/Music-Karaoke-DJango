from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import LoginView, LogoutView
from songs.views import index, landing
from authentication.views import register


class TestUrls(SimpleTestCase):
    def test_login_url_is_resolved(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_register_url_is_resolved(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def test_logout_url_is_resolved(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)

    def test_landing_url_is_resolved(self):
        url = reverse('landing')
        self.assertEquals(resolve(url).func, landing)

    def test_songs_url_is_resolved(self):
        url = reverse('songs:index')
        self.assertEquals(resolve(url).func, index)

    # TODO ranking url test
    # def test_ranking_url_is_resolved(self):
    #     url = reverse('ranking')
    #     print("*** printing ***")
    #     print(resolve(url).func)
    #     print(index)
    #     self.assertEquals(resolve(url).func, ranking)

    # TODO settings url test
    # def test_settings_url_is_resolved(self):
    #     url = reverse('settings')
    #     print("*** printing ***")
    #     print(resolve(url).func)
    #     print(index)
    #     self.assertEquals(resolve(url).func, settings)
