from django.db import models

# Create your models here.
class Category(models.Model):
    Category_name=models.CharField(max_length=20)
    image=models.ImageField(default='abc.jpg',upload_to='Images')

    def __str__(self):
       return self.Category_name

class meta:
    db_table= "Category"

class Product(models.Model):
    product_name=models.CharField(max_length=500)
    ingredients=models.CharField(max_length=500)
    description=models.CharField(max_length=50000)
    image=models.ImageField(default='abc.jpg',upload_to='Images')
    cat=models.ForeignKey(to='Category',on_delete=models.CASCADE)

    class Meta:
        db_table="Product"   

class UserInformation(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=20)

    class Meta:
        db_table="UserInformation"    