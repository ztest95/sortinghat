from django.contrib import admin
from django.urls import path, include

import sortinghat.views as views

urlpatterns = [
    path('', views.home, name='home'),
]
