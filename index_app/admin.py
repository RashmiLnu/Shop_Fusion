from django.contrib import admin
from index_app.models import Product, Orders, OrderUpdate, ContactUs

# Register your models here.
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(ContactUs)

