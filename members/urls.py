from django.urls import path

from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #login/logout/register
    path('login_user', views.login_user, name='login'),
    path('logout_user', views.logout_user, name='logout'),
    path('register_user', views.register_user, name='register'),
    path('login_doctor', views.login_doctor, name='login_doctor'),
    path('logout_doctor', views.logout_doctor, name='logout_doctor'),
    path('register_doctor', views.register_doctor, name='register_doctor'),
]