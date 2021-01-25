from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render

def login(request):
    tip=''
    if request.method =='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    tip='登录成功'
                    return render(request,"indexApp.html")
                else:
                    tip='账户未激活'
            else:
                tip='用户名或密码错误'
        else:
            tip='用户名不存在'
    else:
        tip='请求错误'

# Create your views here.
def register(request):
    tip=''
    if request.method=='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if User.objects.filter(username=username):
            tip='用户名已存在'
        else:
            user=User.objects.create_user(username=username,password=password)
            user.save()
            tip='注册成功,请登录'
        return
def login(request):
    return render(request, 'indexApp/login.html')