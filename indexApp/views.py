import json

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render

#判断用户是否登录状态 登录返回True 否则返回False
def isLogin(request):
    if request.user.is_authenticated:
        return True;
    else:
        return False;

def index(request):
    if isLogin(request):
        #如果用户 已经登录过了 返回首页 否则返回登录页
        return render(request, "index.html")
    else:
        return render(request, 'login.html')

def user_login(request):
    '''状态码 登录成功：200 密码错误：400 账户未激活：301 '''
    res = {"code": 200, "msg": ""}
    if request.method =='POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        print("用户名",username)
        print("密码",password)
        #验证用户名密码是否正确
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                #使用内置login函数登录 返回值：session, META, csrf_cookie_needs_reset
                login(request, user)
                #登录成功返回首页
                # return render(request,"index.html")
                ##2021年2月2日11:53:07 修改为ajax 登录成功返回code = 200
                res['code'] = 200 ;
                res['msg'] = "登录成功"
            else:
                #create_user 创建新用户的时候 is_active 默认是1，也就是True
                res['code'] = 301 ;
                res['msg'] = "账户未激活";
        else:
            res['code'] = 400 ;
            res['msg'] = "用户名或密码错误"
    elif request.method =='GET':
        return redirect("/login")#如果是get 就返回登录界面
    #In order to allow non-dict objects to be serialized set the safe parameter to False. 添加safe=False
    print(res);
    return JsonResponse(res,safe=False)

# 注销
def user_logoutAction(request):
    logout(request)
    return redirect("/login")


def user_register(request):
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
