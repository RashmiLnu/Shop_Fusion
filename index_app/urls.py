

from django.contrib import admin
# from django.urls import path
from index_app import views

# urlpatterns = [
#    path("home/", views.home, name="home"),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("contact_us/", views.contact_us, name="contact_us"),
    # path('submit_contact/', views.submit_contact, name='submit_contact'),

    
]
    

