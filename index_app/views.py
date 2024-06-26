from django.contrib import messages
from .models import ContactUs
from math import ceil
from django.contrib import messages
from django.shortcuts import redirect, render
from index_app.models import OrderUpdate, Orders, Product
from index_app.models import Orders
from django.http import JsonResponse
from django.core import serializers


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

    return render(request, "home.html",params)

def checkout(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Login & Try Again")
        return redirect('/authCart/login')

    if request.method=="POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amt')
        email = request.POST.get('email', '')
        address1 = request.POST.get('address1', '')
        address2 = request.POST.get('address2','')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        Order = Orders(items_json=items_json,name=name,amount=amount, email=email, address1=address1,address2=address2,city=city,state=state,zip_code=zip_code,phone=phone)
        print(amount)
        Order.save()
        update = OrderUpdate(order_id=Order.order_id,update_desc="the order has been placed")
        update.save()
        thank = True
# # # PAYMENT INTEGRATION

        id = Order.order_id
        oid=str(id)+"ShopyCart"
        param_dict = {
            'ORDER_ID': oid,
            'TXN_AMOUNT': str(amount),
            'CUST_ID': email,
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
        }

        handlerequest_result = handlerequest(request, param_dict)  # Assign the result of the handlerequest function to a variable
        param_dict['CALLBACK_URL'] = handlerequest_result  # Use the result as the value for the 'CALLBACK_URL' key

        # param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
        return render(request, 'paymentstatus.html',{'response': param_dict})

    return render(request, 'checkout.html')

# @csrf_exempt
def handlerequest(request,param_dict):
   
    response_dict = {'RESPCODE':'01'}
    
    verify = True
    if verify:
        if response_dict['RESPCODE'] == '01':
            a=param_dict.get('ORDER_ID')
            b=param_dict.get('TXNAMOUNT')
            rid=int(a.replace("ShopyCart",""))

            # Update response_dict with ORDERID and TXNAMOUNT
            response_dict = {
                'RESPCODE':'01',
                'ORDERID': a,
                'TXNAMOUNT': b
            }

            print(rid)
            filter2= Orders.objects.filter(order_id=rid)
            print(filter2)
            print(a,b)
            for post1 in filter2:

                post1.oid=a
                post1.amountpaid=b
                if response_dict['RESPCODE'] == '01':
                    post1.paymentstatus="PAID"
                else:
                    post1.paymentstatus="UNPAID"
                post1.save()

        
    return render(request, 'paymentstatus.html', {'response': response_dict})



def api_products(request):
    products = Product.objects.all()
    print(products)
    products_json = serializers.serialize('json', products)
    print(products_json)
    return JsonResponse(products_json, safe=False)
