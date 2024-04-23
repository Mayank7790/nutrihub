from django.db import models
class Food(models.Model):
    Id=models.AutoField
    Food_Name=models.CharField(max_length=120)
    Food_Description=models.CharField(max_length=200,default="")
    Category=models.CharField(max_length=20,default="")
    sub_categoty = models.CharField(max_length=20, default="")
    Price=models.IntegerField(default="0")
    Product_image=models.ImageField(upload_to="shop/images",default="")
    product_Date=models.DateField()
    def __str__(self):
         return  self.Food_Name
class Contact(models.Model):
    msgid=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50 ,default="")
    Email = models.CharField(max_length=70,default="")
    Mobile = models.IntegerField(default="0")
    Message= models.CharField(max_length=7000,default="")
    def __str__(self):
         return  self.Name
class Product_order(models.Model):
    orderid=models.AutoField(primary_key=True)
    Name = models.CharField(max_length=50 ,default="")
    Email = models.CharField(max_length=70,default="")
    Mobile = models.CharField( max_length=70 ,default="0")
    Address= models.CharField(max_length=7000,default="")
    City=models.CharField(max_length=50, default="")
    State=models.CharField(max_length=30, default="")
    Zip=models.CharField(max_length=10, default="")
    Country = models.CharField(max_length=10, default="")
    Orders_name = models.CharField(max_length=1000000000,default="")
    Orders_quantity = models.CharField(max_length=1000000000,default="")
    Orders_price = models.CharField(max_length=1000000000,default="")
    Orders_mode = models.CharField(max_length=1000000000,default="")
    Orders_img = models.CharField(max_length=1000000000,default="")
    order_Description = models.CharField(max_length=150, default="your order is placed")
    Date = models.DateField(auto_now=True, blank=True)
    Time = models.TimeField(auto_now=True, blank=True)
    def __str__(self):
         return  self.Name
class Register(models.Model):
    Id=models.AutoField
    Name=models.CharField(max_length=120)
    email=models.CharField(max_length=20,default="")
    Mobile = models.CharField(max_length=20, default="")
    Address = models.CharField(max_length=20, default="")
    password=models.CharField(max_length=20,default="")
    def __str__(self):
         return  self.Name
class Review(models.Model):
    Id=models.AutoField
    Name=models.CharField(max_length=120)
    product_id=models.CharField(max_length=20,default="")
    review=models.CharField(max_length=20,default="")
    rating=models.CharField(max_length=20,default="")
    def __str__(self):
         return  self.Name