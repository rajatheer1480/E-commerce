from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from shopping.models import Account
# Create your views here.

####LOGIN VIEW##########


def Login_View(request):
    if request.method=='POST':
        uname = request.POST['username']
        upass = request.POST['password']
        user= authenticate(username=uname,password=upass)
        if user is not None:
            login(request,user)
            messages.success(request,'User is Login Successsfully')
            return redirect('/')
        else:
            messages.warning(request,'Invaild  Credentials')
            return redirect('login')
    return render(request,'account/login.html')



#####SING-UP#####

def SignUp_View(request):
    if request.method =='POST':
        uname= request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        upass = request.POST.get('password')
        if User.objects.filter(email=email).exists():
            messages.warning(request,'Email already Exists')
            return redirect('login')
        else:
            user = User(username=uname,password=upass,first_name=first_name,last_name=last_name,email=email)
            user.set_password(upass)
            user.save()
            messages.success(request,'User Register successfully')
            return redirect('login')

    return render(request,'account/sign-up.html')


######LOGOUT VIEW#######

def Logout_View(request):
    logout(request)
    return redirect('login')
    