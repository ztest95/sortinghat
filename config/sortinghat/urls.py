from django.contrib import admin
from django.urls import path, include

import sortinghat.views as views

urlpatterns = [
    path('', views.sortinghat, name='sortinghat'),
    # path('api/sortinghat/<str:name>', views.getHouse, name='getHouse'),
]
