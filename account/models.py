from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractBaseUser,AbstractUser
from django.utils import timezone
# from shopping.managers import MyAccountManager
from django.contrib.auth.models import PermissionsMixin, User
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

# class Account(AbstractBaseUser, PermissionsMixin):
#     """
#     Custom user model for strive saving application
#     users.
#     """
#     email = models.EmailField(max_length=255, unique=True)
#     username = models.CharField(max_length=255, unique=True)
#     mobile = models.CharField(max_length=15, null=True, blank=True)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255, null=True,blank=True)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     last_login = models.DateTimeField(auto_now_add=True)
#     is_admin = models.BooleanField(default=False)
#     is_staff = models.BooleanField(default=False)
#     is_superuser = models.BooleanField(default=False)
#     is_active = models.BooleanField(default=True)
#     avtar = models.ImageField(upload_to ='avtar/images',null= True,blank = True)
#     objects = MyAccountManager()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS =   ['username']

#     def __str__(self):
#         return "#ID%s-%s" % (self.id, self.email)

#     class Meta:
#         verbose_name = "Account"
#         verbose_name_plural = "Accounts"

