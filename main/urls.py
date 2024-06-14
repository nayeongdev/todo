from django.contrib.auth import views
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('todo-create/', views.TodoCreate.as_view(), name='todo_create'),
    path('todo-update/<int:pk>', views.TodoUpdate.as_view(), name='todo_update'),
    path('todo-delete/<int:pk>', views.TodoDelete.as_view(), name='todo_delete'),
    path('task-update/<int:pk>', views.TaskUpdate.as_view(), name='task_update'),
    path('task-delete/<int:pk>', views.TaskDelete.as_view(), name='task_delete'),
]
