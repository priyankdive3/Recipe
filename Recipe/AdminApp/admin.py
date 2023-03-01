from django.contrib import admin
from .models import Category,Product,UserInformation
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display=("Category_name",)

class ProductAdmin(admin.ModelAdmin):
    list_display=("product_name","image","ingredients","description","cat")

class UserInformationAdmin(admin.ModelAdmin):
    list_display=("username","email","password")
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(UserInformation,UserInformationAdmin)

