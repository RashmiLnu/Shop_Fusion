from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message_type = models.CharField(max_length=255)
    other_message = models.TextField()

    def __str__(self):
        return str(self.name)

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    product_category = models.CharField(max_length=50, default="")
    product_subcategory = models.CharField(max_length=50, default="")
    product_description = models.CharField(max_length=300)
    product_image = models.ImageField(upload_to="products_img")

    def __str__(self):
        return str(self.product_name) 
    
class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json =  models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)    
    oid=models.CharField(max_length=150,blank=True)
    amountpaid=models.CharField(max_length=500,blank=True,null=True)
    paymentstatus=models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=100,default="")

    def __str__(self):
        return str(self.name)


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    delivered=models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.update_desc)[:7] + "..."
