from django.contrib import admin

# Register your models here.
from .models import *
# from account.models import Account
from django.contrib.auth.admin import UserAdmin
# Register your models here.


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
