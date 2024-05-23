from django.test import TestCase
from django.urls import reverse

from main.models import Todo


class TodoTestCase(TestCase):

    def test_todo_view(self):
        """
        메인 페이지 접근 테스트
        """
        response = self.client.get(reverse('main:home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/home.html')

    def test_create_todo(self):
        """
        todo 생성 테스트
        """
        response = self.client.post(reverse('main:todo_create'), {'title': 'test'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('main:home'))
