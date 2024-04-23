from django.core.mail import EmailMessage
from django.urls import path
from authCart import views

urlpatterns = [
   path("signup/", views.signUp , name="signUp"),
   path("login/", views.handle_login , name="handle_login"),
   path("logout/", views.handle_logout , name="handle_logout"),
     
]