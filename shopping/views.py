from django.shortcuts import render,redirect
from django.views import View
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required 
from shopping.models import Product,Category,Cart,Customer
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from .serializers import CustomerSerializer

## HOMEVIEW###

# @method_decorator(login_required, name ='dispatch')
class Home_View(View):
    template_name='shopping/index.html'
    def get(self,request):
        # prod = Product.objects.all()
        category = Category.objects.all()
        categoryID = request.GET.get('category')
        if categoryID:
            prod = Product.objects.filter(category=categoryID)
        else:
            prod=Product.objects.all()

            ####ADD Paginations#######
            prod = Product.objects.all()
            page = request.GET.get('page', 1)
            paginator = Paginator(prod, 3)
            try:
                prod = paginator.page(page)
            except PageNotAnInteger:
                prod = paginator.page(1)
            except EmptyPage:
                prod = paginator.page(paginator.num_pages)    
                    

                
                ######SEARCHING########
        if request.method=='GET':
            pt= request.GET.get('product_name')
            if pt!=None:
                prod = Product.objects.filter(product_name__icontains=pt)
                print(prod)

        context={
            'prod':prod,
            'category':category,
                
        }
        
        return render(request,self.template_name,context)



########SHOP#######

class Shop_View(View):
    template_name='shopping/shop.html'
    def get(self,request):
        # # prod= len(Cart.objects.filter(user=request.user))
        # customer= Customer.objects.all()

        prod = Product.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(prod, 10)
        try:
            prod = paginator.page(page)
        except PageNotAnInteger:
            prod = paginator.page(1)
        except EmptyPage:
            prod = paginator.page(paginator.num_pages)   
       
        return render(request,self.template_name,{'prod':prod})




# def Shop_View(request):
   
    
#     return render(request,'shopping/shop.html')


########SHOP-DETAIL#######

class ShopDetail_View(View):
    template_name='shopping/detail.html'
    def get(self,request,id =None):
        prod= Product.objects.filter(id=id)
        
        return render(request,self.template_name,{'prod':prod})

# class ShopDetail_View(View):
#     template_name='shopping/detail.html'
#     def get(self,request):
#         prod = Product.objects.all()
#         return render(request,self.template_name,{'prod':prod})

        
       
    

########CONTACT#######

class Contact_View(View):
    template_name='shopping/contact.html'
    def get(self,request):
        return render(request,self.template_name)




########CheckOut#######

class CheckOut_View(View):
    template_name='shopping/checkout.html'
    def get(self,request):
        return render(request,self.template_name)



########ADD CART#######

class Cart_View(View):
    template_name='shopping/cart.html'
    def get(self,request):        
        user = request.user
        product = Cart.objects.filter(user=user)
        total_item = len(Cart.objects.filter(user=request.user))
        amount = 0.0
        shipping_amount = 50.0
        total_amount = 0.0
        cart_price = [p for p in Cart.objects.all() if p.user == user]

        if cart_price:
            for p in cart_price:
                temp_amount = (p.quantity * p.product.price)
               
                amount += temp_amount
                total_amount = amount + shipping_amount
                print(total_amount)
                
            context={
                'product':product,
                'total_amount' : total_amount,
                'amounts':amount,
                'total_item': total_item,
            }
       
        return render(request,self.template_name,context)


def Add_to_cart(request, id=None):
    product = Product.objects.get(id=id)
    if Cart.objects.filter(product=product).exists():
        # messages.warning(request,'already add to cart')
        return redirect('cart')
    else:
        ncart = Cart.objects.create(user=request.user,product=product)
        ncart.save()
        return redirect('home')
    

     

def Increment(request, id):
    if request.method == "GET":
        item = Cart.objects.get(id=int(id))
        if 0 < (item.quantity + 1) <= item.product_id.quantity:
            item.quantity += 1
            item.save()
            print(item)
            return redirect('cart')
    return redirect('cart')



# def Decrement(request, id):
#     if request.method == "GET":
#         item = Cart.objects.get(id=int(id))
#         if 0 < (item.quantity - 1) <= item.product_id.quantity:
#             item.quantity -= 1
#             item.save()
#             return redirect('cart')
#     return redirect('cart')

def Delete(request,id=None):
    prod=Cart.objects.get(id=id)
    prod.delete()
    return redirect('cart')
    




#####SHOW CART VIEW#########


# class Show_cart(View):
#     template_name = 'shopping/cart.html'
#     def get (self,request):
    
#         user = request.user
#         cart = Cart.objects.filter(user=user)
#         total_item = len(Cart.objects.filter(user=request.user))
#         amount = 0.0
#         shipping_amount = 50.0
#         total_amount = 0.0
#         cart_price = [p for p in Cart.objects.all() if p.user == user]

#         if cart_price:
#             for p in cart_price:
#                 temp_amount = (p.quantity * p.product.price)
#                 amount += temp_amount
#                 total_amount = amount + shipping_amount
#                 print(total_amount)
#             context = {
#                 'cart':cart,
#                 'total_amount' : amount + shipping_amount,
#                 'amounts':amount,
#                 'total_item': total_item,
#             }
#         return render (request,self.template_name,context)

       


####CUSTOMERSERIALIZER###


class Customer(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class=  CustomerSerializer
   

   
