from django.contrib import admin
from django.urls import path, include

import link.views as views
import sortinghat.views 
urlpatterns = [

    path('home', views.home, name='home'),
    path('u/<str:user>', views.view_links, name='view_links'),
    path('generate-link', views.generate_link, name='generate_link'),
    path('hat/<str:uuid>/', views.open_link, name='open_link'),
    path('hat/<str:uuid>/view-names', views.sh_view_names, name='view_names'),
    path('hat/<str:uuid>/add-names', views.sh_add_names, name='add_name'),
    path('hat/<str:uuid>/delete-name/<str:id>', views.sh_delete_name, name='delete_name'),
    path('api/sortinghat/<str:name>', sortinghat.views.getHouse),
]
