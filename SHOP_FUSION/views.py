from django.shortcuts import render
import requests

def about(request):
    return render(request, "about.html")


def team(request):
    return render(request, "team.html")

def products(request):
    return render(request, "products.html")

def product_api(request):
    response = requests.get('https://fakestoreapi.com/products')  # Replace with your API URL
    products = response.json()
    return render(request, "product_api.html", {'products': products})


   
