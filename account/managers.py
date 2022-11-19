
# from django.contrib.auth.base_user import BaseUserManager
# from django.core.exceptions import ValidationError
# from django.contrib.auth.models import PermissionsMixin, User



# # class MyAccountManager(BaseUserManager):
# #     """
# #     Custom user model manager for all strive users
# #     """

# #     def create_user(self, email, first_name, password=None):
# #         if not email:
# #             raise ValidationError("Email is required.")
# #         if not first_name:
# #             raise ValidationError("First Name is required.")
# #         if not password or password is None:
# #             raise ValidationError("Password is required.")
        
# #         user = self.model(email=self.normalize_email(email), first_name=first_name)
# #         user.set_password(password)
# #         user.save(using=self._db)
# #         return user

# #     def create_superuser(self, email, first_name, password=None):
# #         user = self.create_user(email=email, first_name=first_name,
# #                                 password=password)
# #         user.is_superuser = True
# #         user.is_staff = True
# #         user.save(using=self._db)
# #         return user

# class MyAccountManager(BaseUserManager):
#     def create_user(self, email,username,password = None):
#         if not email:
#             raise ValidationError('Email is required')
#         if not username:
#             raise ValidationError('Username is required')
#         user = self.model(email=self.normalize_email(email),
#         username = username,
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self,email,username, password):
#         user = self.create_user(email=self.normalize_email(email),
#             username= username,
#             password = password)
#         user.is_admin = True
#         user.is_superuser= True
#         user.is_staff = True
#         user.set_password(password)
#         user.save(using= self._db)
#         return user 

