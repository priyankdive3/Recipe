from django.contrib import admin
from .models import Category,Product,UserInformation,Ingredients
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=("Category_name",)

class ProductAdmin(admin.ModelAdmin):
    list_display=("product_name","image","ingredients","description","small_description","cat")

class UserInformationAdmin(admin.ModelAdmin):
    list_display=("username","email","password")

class IngredientsAdmin(admin.ModelAdmin):
    list_display=("item_name","price","sale_price","image","description","quantity")


admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Ingredients,IngredientsAdmin)
admin.site.register(UserInformation,UserInformationAdmin)

