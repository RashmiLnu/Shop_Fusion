from django.db import models

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