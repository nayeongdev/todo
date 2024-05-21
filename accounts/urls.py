from django.contrib.auth import views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('<str:username>/', views.profile, name='profile'),
]