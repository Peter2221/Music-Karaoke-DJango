from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from authentication.models import Profile
from .views import save_in_database


class RankingTest(TestCase):
    def test_show_ranking(self):
        response = self.client.get(reverse('ranking:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ranking.html')
