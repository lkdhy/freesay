from django.shortcuts import render
from django.http import HttpResponse
# 我们只要用 JsonResponse 返回 Json 对象即可，其直接接收Python的字典
from django.http import JsonResponse
import json

# Create your views here.

# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    data = json.loads(request.body)
    return JsonResponse({
        'success': True,
        'messsage': '恭喜！登陆成功~',
        'username': data.get('username', 'WTF, no username?!'),
        'password': data.get('password', 'WTF, no password?!')
    })

def hello(request):
    return JsonResponse({
        'success': True, 
        'message': '你好，我是用 Django 写的后端。我们交互成功了！'
    })