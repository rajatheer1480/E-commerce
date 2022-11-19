from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from account import views

urlpatterns = [
    path('login/',views.Login_View,name='login'),
    path('sign-up/',views.SignUp_View,name='sign-up'),
    path('logout/',views.Logout_View,name='logout'),
    
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
