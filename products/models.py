from django.db import models

# Create your models here.

class Product_Category(models.Model):

    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category



class Products(models.Model):

    product_name = models.CharField(max_length=255,unique=True)
    product_cat = models.ForeignKey(Product_Category,on_delete=models.CASCADE)
    product_price = models.IntegerField()
    product_image = models.ImageField()
    product_desc = models.TextField()

    def __str__(self):

        return self.product_name


