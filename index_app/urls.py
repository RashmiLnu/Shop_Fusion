

from django.contrib import admin
from django.urls import path
from index_app import views


urlpatterns = [
    path("", views.home, name="home"),
    path("contact_us/", views.contact_us, name="contact_us"),
    path("checkout/", views.checkout, name="Checkout"),
    path('api/products/', views.api_products, name='api_products'),
   
]
    

