from django.shortcuts import render
from django.contrib import messages
from .models import ContactUs


def home(request):
    return render(request, "base.html")


def contact_us(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message_type = request.POST.get("message_type")
        other_message = request.POST.get("other_message")
        contact_us = ContactUs(name=name, email=email, message_type=message_type, other_message=other_message)
        contact_us.save()
        messages.info(request, "Your message has been sent successfully")
        return render(request, "contact_us.html")
    return render(request, "contact_us.html")



