from django.shortcuts import render
from django.http import HttpResponse
# 我们只要用 JsonResponse 返回 Json 对象即可，其直接接收Python的字典
from django.http import JsonResponse
import json
from .models import *
from django.core.serializers import serialize
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def logout(request):
    if 1 > 0:
        return JsonResponse({
            'success': True,
            'message': '登出成功'
        })
    else:
        return JsonResponse({
            'success': False,
            'message': '莫名其妙地登出失败'
        })

def login(request):
    data = json.loads(request.body)
    u = data.get('username', 'WTF, no username?!')
    p = data.get('password', 'WTF, no password?!')
    #print(1, u, p)
    find_user = User.objects.filter(username=u, user_pwd=p).count()
    #print(find_user)
    if find_user > 0:
        return JsonResponse({
            'success': True,
            'message': '恭喜！登陆成功~',
            'username': data.get('username', 'WTF, no username?!'),
            'password': data.get('password', 'WTF, no password?!')
        })
    else:
        return JsonResponse({
            'success': False,
            'message': '骚瑞，密码或用户名错误了~',
            'username': data.get('username', 'WTF, no username?!'),
            'password': data.get('password', 'WTF, no password?!')
        })

def hello(request):
    #print(2)
    return JsonResponse({
        'success': True, 
        'message': '你好，我是用 Django 写的后端。我们交互成功了！'
    })

def register(request):
    #print(3)
    data = json.loads(request.body)
    username = data.get('username', 'WTF, no username?!')
    pwd = data.get('password', 'WTF, no password?!')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')
    email = data.get('email', '')
    #print(u, p)
    if username and pwd:
        stu = User(username=username, user_pwd=pwd, first_name=first_name, last_name=last_name, email=email)
        stu.save()
        return JsonResponse({
            'success': True,
            'message': '你好，我是用 Django 写的后端。我们交互成功了！'
        })
    else:
        return JsonResponse({
            'success': False,
            'message': '请输入完整信息！'
        })

def userslist(request):
    print('enter userslist')
    data = json.loads(request.body)
    pageNumber = data.get('pageNumber')
    number = data.get('number')
    records = User.objects.all().order_by('-user_id')[number * (pageNumber - 1): number * pageNumber]
    print("number:", number)
    #print(records)
    data = serialize('json', records)
    print(data)
    json_data = json.loads(data)
    # 提取每个对象中的 "fields" 字段
    fields_list = []
    for obj in json_data:
        fields_list.append(obj['fields'])
    # data = serialize('array', records)
    count = User.objects.count()
    print("count:", count)
    return JsonResponse({
        'success': True,
        'total_users': count,
        'users': fields_list
    })

