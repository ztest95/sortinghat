from django.contrib import admin
from django.urls import path, include

import link.views as views
import sortinghat.views 
urlpatterns = [
    path('u/<str:user>', views.view_links, name='view_links'),
    path('generate_link', views.generate_link, name='generate_link'),
    path('<str:link>/', views.open_link, name='open_link'),
    path('api/sortinghat/<str:name>', sortinghat.views.getHouse),
]
