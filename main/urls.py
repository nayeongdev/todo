from django.contrib.auth import views
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('todo-create/', views.TodoCreate.as_view(), name='todo_create'),
]