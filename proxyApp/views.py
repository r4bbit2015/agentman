from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from .models import ipList,Record
from django.http import JsonResponse
# Create your views here.
def index(request):
    # return render()
    return render(request, 'proxyApp/index.html')
@csrf_exempt
def api(request):
    data = {
        'status': 200,
        'data': [],
    }
    #用户验证应该单独拉出来写 --by r4bbit
    if request.method=='POST':
        username=request.POST.get('username','')
        password = request.POST.get('password','')
        # print(username)
        # print(password)
        if User.objects.filter(username=username):
            user=authenticate(username=username,password=password)
            if user:
                if user.is_active:
                    login(request,user)
                    data['data']=ip_list(user,request)
                    return JsonResponse(data,content_type='application/json')
                else:
                    data['status']=201
                    data['data']="用户未激活"
                    return JsonResponse(data,content_type='application/json')
            else:
                data['status'] = 202
                data['data'] = "用户名或密码错误"
                return JsonResponse(data, content_type='application/json')
        else:
            data['status'] = 203
            data['data'] = "用户名不存在"
            return JsonResponse(data, content_type='application/json')
    else:
        return render(request, 'proxyApp/index.html')
def ip_list(user,request):
    '''
    只用来判断，post中携带的参数，然后根据参数调用不同的方法
    :param user:
    :param request:
    :return:
    '''
    data_list = []
    repeat=request.POST.get('repeat')
    list = ipList.objects.filter(acc__gt=0)
    for ip in list:
        if repeat == '1':
            if not Record.objects.filter(user=user).filter(ip=ip):
                Record.createRecord(user,ip).save()
                data_list.append(f'{ip.ip}:{ip.port}')
        else:
            data_list.append(f'{ip.ip}:{ip.port}')
        if len(data_list)>=5:
            break
    return data_list
'''
代码还需要进行分模块
需求分析：
    1、提取数量。
    2、指定端口
    3、地区
    4、初始化去重
    
'''