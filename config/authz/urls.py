from django.contrib import admin
from django.urls import path, include

import authz.views as views

urlpatterns = [
    path('login', views.login_user, name='login'),
    path('register', views.register_user, name='register'),
    path('logout', views.logout_user, name='logout'),
]
