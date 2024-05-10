from math import ceil
from django.shortcuts import render
from index_app.models import Product


def home(request):
    allProds = []

    catprods = Product.objects.values('product_category','id')
    print(catprods)
    cats = {item['product_category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(product_category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}

    return render(request, "base.html",params)
