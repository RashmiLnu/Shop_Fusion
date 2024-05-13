from django.shortcuts import redirect, render
import requests
from django.contrib import messages

from index_app.models import OrderUpdate, Orders


def about(request):
    return render(request, "about.html")


def team(request):
    return render(request, "team.html")

def product_api(request):
    response = requests.get('https://fakestoreapi.com/products')  # Replace with your API URL
    products = response.json()
    return render(request, "product_api.html", {'products': products})
   
# def profile(request):
#     if not request.user.is_authenticated:
#         messages.warning(request,"Login & Try Again")
#         return redirect('/authCart/login')
#     currentuser=request.user.username
#     print(currentuser)
#     items=Orders.objects.filter(email=currentuser)
#     for item in items:
#         print(item.oid)
#         myid=item.oid
#         rid=myid.replace("ShopyCart","")
#         print(rid)
#         if rid:  # check if rid is not empty
#             item.status=OrderUpdate.objects.filter(order_id=int(rid))
#             print(item.status)
#         else:
#             item.status = None  # or some default value
#     context ={"items":items}
#     return render(request,"profile.html",context)

def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/auth/login')
    currentuser=request.user.username
    items=Orders.objects.filter(email=currentuser)
    rid=""
    for i in items:
        print(i.oid)
        # print(i.order_id)
        myid=i.oid
        rid=myid.replace("ShopyCart","")
        print(rid)
    if rid:
        status=OrderUpdate.objects.filter(order_id=int(rid))
    else:
        status = OrderUpdate.objects.none()
    for j in status:
        print(j.update_desc)

   
    context ={"items":items,"status":status}
    # print(currentuser)
    return render(request,"profile.html",context)