from datetime import timedelta

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from accounts.models import User
from main.models import Todo, Task
from main.tasks import create_task


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

#
# class TodoTaskTestCase(TestCase):
#
#     def setUp(self):
#         self.email = 'testuser@example.com'
#         self.password = 'testpassword'
#         self.user = User.objects.create_user(email=self.email, password=self.password)
#
#         self.start_date = timezone.now().date()
#         self.end_date = self.start_date + timedelta(days=10)
#         self.todo_daily = Todo.objects.create(
#             user=self.user,
#             title='Daily Task',
#             priority=1,
#             start_date=self.start_date,
#             end_date=self.end_date,
#             interval='daily'
#         )
#         self.todo_no_interval = Todo.objects.create(
#             user=self.user,
#             title='One Time Task',
#             priority=1,
#             start_date=self.start_date,
#             end_date=self.end_date,
#             interval=None
#         )
#
#     def test_create_daily_tasks(self):
#         create_task(self.todo_daily.id)
#
#         tasks = Task.objects.filter(todo=self.todo_daily)
#         self.assertEqual(tasks.count(), 11)  # 10 days + start_date
#
#         task_dates = [task.created_at for task in tasks]
#         expected_dates = [self.start_date + timedelta(days=i) for i in range(11)]
#
#         self.assertEqual(task_dates, expected_dates)
#
#     def test_create_one_time_task(self):
#         create_task(self.todo_no_interval.id)
#
#         tasks = Task.objects.filter(todo=self.todo_no_interval)
#         self.assertEqual(tasks.count(), 1)
#
#         task = tasks.first()
#         self.assertEqual(task.created_at, self.start_date)
#
#     def test_create_indefinite_tasks(self):
#         todo_indefinite = Todo.objects.create(
#             user=self.user,
#             title='Indefinite Task',
#             priority=1,
#             start_date=self.start_date,
#             end_date=None,
#             interval='daily'
#         )
#         create_task(todo_indefinite.id)
#
#         tasks = Task.objects.filter(todo=todo_indefinite)
#         self.assertTrue(tasks.count() > 0)  # Ensure tasks are being created
#
#         # We limit to 1 year (365 days)
#         self.assertEqual(tasks.count(), 366)  # 365 days + start_date
#
#         task_dates = [task.created_at for task in tasks]
#         expected_dates = [self.start_date + timedelta(days=i) for i in range(366)]
#         self.assertEqual(task_dates, expected_dates)
#
#     def test_create_weekly_tasks(self):
#         todo_weekly = Todo.objects.create(
#             user=self.user,
#             title='Weekly Task',
#             priority=1,
#             start_date=self.start_date,
#             end_date=self.end_date,
#             interval='weekly'
#         )
#         create_task(todo_weekly.id)
#
#         tasks = Task.objects.filter(todo=todo_weekly)
#         self.assertEqual(tasks.count(), 2)  # 2 weeks + start_date
#
#         task_dates = [task.created_at for task in tasks]
#         expected_dates = [self.start_date, self.start_date + timedelta(weeks=1)]
#         self.assertEqual(task_dates, expected_dates)
#
#     def test_create_monthly_tasks(self):
#         todo_monthly = Todo.objects.create(
#             user=self.user,
#             title='Monthly Task',
#             priority=1,
#             start_date=self.start_date,
#             end_date=self.start_date + timedelta(days=91),  # Roughly 3 months
#             interval='monthly'
#         )
#         create_task(todo_monthly.id)
#
#         tasks = Task.objects.filter(todo=todo_monthly)
#         self.assertEqual(tasks.count(), 4)  # 3 months + start_date
#
#         task_dates = [task.created_at for task in tasks]
#         expected_dates = [
#             self.start_date,
#             self.start_date + timedelta(days=30),
#             self.start_date + timedelta(days=60),
#             self.start_date + timedelta(days=90),
#         ]
#
#         self.assertEqual(task_dates, expected_dates)
