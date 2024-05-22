from django.test import TestCase, Client
from django.urls import reverse

from .models import User


class LoginTestCase(TestCase):
    def setUp(self):
        self.email = 'testuser@example.com'
        self.password = 'testpassword'
        self.user = User.objects.create_user(email=self.email, password=self.password)

    def test_login_view(self):
        """
        로그인 페이지 접근 테스트
        """
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_login_success(self):
        """
        로그인 성공 테스트
        """
        login_data = {
            'username': self.email,
            'password': self.password
        }
        response = self.client.post(reverse('accounts:login'), login_data)
        self.assertTrue(response.wsgi_request.user.is_authenticated)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main:home'))

    def test_login_failure(self):
        """
        로그인 실패 테스트
        """
        login_data = {
            'username': self.email,
            'password': self.password
        }
        response = self.client.post(reverse('accounts:login'), login_data, follow=True)
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_view(self):
        """
        로그아웃 테스트
        """
        self.client.login(username='testuser@example.com', password='testpassword')
        response = self.client.get(reverse('accounts:logout'), follow=True)
        self.assertFalse(response.wsgi_request.user.is_authenticated)
        self.assertRedirects(response, reverse('accounts:login'))
