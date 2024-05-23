from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.SigninView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('password-change/', views.ChangePasswordView.as_view(), name='password_change'),
]
