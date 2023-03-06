from django.db import models
from AdminApp.models import UserInformation, Ingredients    

# Create your models here.
class MyCart(models.Model):
    users = models.ForeignKey(to='AdminApp.UserInformation', on_delete=models.CASCADE)
    items = models.ForeignKey(to='AdminApp.Ingredients', on_delete=models.CASCADE)
    qty = models.IntegerField()

    class Meta:
        db_table = "MyCart"