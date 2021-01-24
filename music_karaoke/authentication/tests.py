from django.test import TestCase
from django.contrib.auth.models import User

#tests need to start with word test like in test_login
#example test to check github actions
class UserTestCase(TestCase):
    def test_login(self):
        one = 1
        also_one = 1
        self.assertEqual(one,also_one)

