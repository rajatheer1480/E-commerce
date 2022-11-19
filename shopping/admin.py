from django.contrib import admin

# Register your models here.

from .models import *
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from shopping.models import Product,Customer,Category,Colorvarient,Sizevarient,Cart

# Register your models here.

# Register your models here.
# class AccountAdmin(UserAdmin):
#     list_display = ['email','username','date_joined','last_login','is_admin','is_staff','is_admin']
#     search_fields =['email','username']
#     readonly_fields =('id','date_joined','last_login')
#     filter_horizontal=()
#     list_filter = ()
#     fieldsets = ()
# admin.site.register(Account,AccountAdmin)

######PRODUCT#####
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('id','product_name','category','description','price','image')
    search_fields= ('product_name','category')

###CATEGORY#######

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name')
   
######CUSTOMER####

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display=('id','user','first_name','last_name','mobile','city','address','state','zip_code','email')
    search_fields= ['id','first_name','mobile']

#####SIZEVARIENT#####
@admin.register(Sizevarient)
class SizeVarientAdmin(admin.ModelAdmin):
    list_display=('size','price')
    search_fields= ['size']




#####COLORVARIENT#####
@admin.register(Colorvarient)
class ColorVarientAdmin(admin.ModelAdmin):
    list_display=('color_name','price')
    search_fields= ['color_name']
###ADD CART######

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=('id','user','product','quantity')
    