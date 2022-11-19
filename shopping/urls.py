from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from shopping import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('customerapi',views.Customer,basename='customer'),

urlpatterns = [
    path('',views.Home_View.as_view(),name='home'),
    path('shop/',views.Shop_View.as_view(),name='shop'),
    # path('shop/',views.Shop_View,name='shop'),
    
    path('shop-detail/',views.ShopDetail_View.as_view(),name='shop-detail'),
    path('shop-detail/<int:id>/',views.ShopDetail_View.as_view(),name='shop-detail'),
    path('contact/',views.Contact_View.as_view(),name='contact'),
    path('checkout/',views.CheckOut_View.as_view(),name='checkout'),
    path('cart/',views.Cart_View.as_view(),name='cart'),
    # path('cart/<int:id>/',views.Cart_View.as_view(),name='cart'),
    path('add-to-cart/<int:id>/',views.Add_to_cart,name='add-to-cart'),

    path('increment/',views.Increment,name='increment'),
    # path('decrement/',views.Decrement,name='decrement'),
    path('delete/<int:id>/',views.Delete,name='delete'),
    # path('show-cart/',views.Show_cart.as_view(),name='show-cart'),
    

    path('api/v1/',include(router.urls)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

