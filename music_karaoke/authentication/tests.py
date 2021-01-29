from django.test import TestCase
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.models import User
import os
from django.conf import settings
from .forms import RegisterForm, ProfileForm


class UserTestCase(TestCase):
    def setUp(self):
        self.register_url = reverse('register')
        self.file_photo_path = os.path.join(
            settings.BASE_DIR, 'authentication/test_media/test.jpg')
        self.user = {
            'username': 'test_username',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name',
            'email': 'test@test.pl',
            'password1': 'TestPassword123!$',
            'password2': 'TestPassword123!$',
        }

    def test_user_can_view_page(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

    def test_user_form(self):
        form = RegisterForm(self.user)
        self.assertTrue(form.is_valid)

    def test_profile_form(self):
        with open(self.file_photo_path, 'rb') as f:
            data = {
                'user': self.user,
                'profile_pic': SimpleUploadedFile('test.jpg', f.read())
            }
            form = ProfileForm(data)
            self.assertTrue(form.is_valid)
    
    def test_register_POST_not_valid(self):
        response = self.client.post(self.register_url)
        self.assertEqual(response.status_code, 200)

    def test_register_user_authenticated(self):
        super_user = User.objects.create_superuser(
            username="admin",
            password="admin",
            email="admin@example.com")
        self.client.force_login(super_user)
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 302)

