from django.shortcuts import render
from django.http import HttpResponse
# 我们只要用 JsonResponse 返回 Json 对象即可，其直接接收Python的字典
from django.http import JsonResponse
import json
from .models import *
# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    data = json.loads(request.body)
    u = data.get('username', 'WTF, no username?!')
    p = data.get('password', 'WTF, no password?!')
    print(1, u, p)
    find_user = StudentInfo.objects.filter(stu_name=u, stu_pwd=p).count()
    print(find_user)
    if find_user > 0:
        return JsonResponse({
            'success': True,
            'messsage': '恭喜！登陆成功~',
            'username': data.get('username', 'WTF, no username?!'),
            'password': data.get('password', 'WTF, no password?!')
        })
    else:
        return JsonResponse({
            'success': False,
            'messsage': '骚瑞，密码或用户名错误了~',
            'username': data.get('username', 'WTF, no username?!'),
            'password': data.get('password', 'WTF, no password?!')
        })

def hello(request):
    print(2)
    return JsonResponse({
        'success': True, 
        'message': '你好，我是用 Django 写的后端。我们交互成功了！'
    })

def register(request):
    print(3)
    data = json.loads(request.body)
    u = data.get('username', 'WTF, no username?!')
    p = data.get('password', 'WTF, no password?!')
    print(u, p)
    if u and p:
        stu = StudentInfo(stu_name=u, stu_pwd=p)
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