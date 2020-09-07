from django.contrib.auth import authenticate,login,logout
from django.http import Http404,HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request,"users/login.html",{"message":None})

    context = {
        "user":request.user
    }
    return render(request,"users/user.html",context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    #验证用户身份
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request,user)
        #返回原来的界面
        return HttpResponseRedirect(reverse("index"))
    else:
        #返回登录界面，信息变为 Invalid credentials.
        return render(request,"users/login.html",{"message":"Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request,"users/login.html",{"message":"Logged out."})