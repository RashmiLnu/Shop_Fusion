

# from django.contrib import admin
# from django.urls import path
# from index_app import views

# urlpatterns = [
#    path("home/", views.home, name="home"),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    
]
