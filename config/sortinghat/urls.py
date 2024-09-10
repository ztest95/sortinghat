from django.contrib import admin
from django.urls import path, include

import sortinghat.views as views

urlpatterns = [
    path('', views.sortinghat, name='home'),
    path('', views.sortinghat, name='sortinghat'),
    path('view-names', views.view_names, name='view_names'),
    path('add-name', views.add_name, name='add_name'),
    path('delete-name/<str:id>', views.delete_name, name='delete_name'),
    path('api/sortinghat/<str:name>', views.getHouse, name='getHouse'),
]
