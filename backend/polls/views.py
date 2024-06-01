from django.shortcuts import render
from django.http import HttpResponse
# 我们只要用 JsonResponse 返回 Json 对象即可，其直接接收Python的字典
from django.http import JsonResponse
import json
from .models import *
from django.core.serializers import serialize
import random
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
        user = User.objects.filter(username=u)[0]
        return JsonResponse({
            'success': True,
            'message': '恭喜！登陆成功~',
            'userinfo': {
                'username': user.username,
                'avatar': user.avatar,
                'signature': user.signature,
                'email': user.email,
            }
        })
    else:
        return JsonResponse({
            'success': False,
            'message': '骚瑞，密码或用户名错误了~',
        })

def hello(request):
    #print(2)
    return JsonResponse({
        'success': True, 
        'message': '你好，我是用 Django 写的后端。我们交互成功了！'
    })

def random_avatar():
    # 注意用 utf-8 编码
    with open('polls/avatars.txt', encoding='utf-8') as avatar_file:
        avatar_urls = avatar_file.readlines()
        # print(avatar_urls, avatar_urls.index('###'))
        # print(avatar_urls[0:avatar_urls.index('###\n')])
    return random.choice(avatar_urls[0:avatar_urls.index('###\n')])

def register(request):
    '''
        用户注册时后端给他随机一个头像
    '''
    avatar = random_avatar()
    data = json.loads(request.body)
    username = data.get('username', 'WTF, no username?!')
    pwd = data.get('password', 'WTF, no password?!')
    first_name = data.get('first_name', '')
    last_name = data.get('last_name', '')
    email = data.get('email', '')
    #print(u, p)
    if username and pwd and first_name and last_name and email:
        find_user = User.objects.filter(username=username).count()
        if find_user > 0:
            return JsonResponse({
                'success': False,
                'message': 'sorry~ 该用户名已被注册，请重新输入~'
            })
        stu = User(
            username=username, user_pwd=pwd, avatar=avatar,
            first_name=first_name, last_name=last_name, email=email
        )
        stu.save()
        return JsonResponse({
            'success': True,
            'message': '你好，我是用 Django 写的后端。我们交互成功了！',
            'total_users': User.objects.count()
        })
    else:
        return JsonResponse({
            'success': False,
            'message': '请输入完整信息！'
        })

# 已增加头像
def userinfo(request):
    print('enter getuserinfo')
    username = request.GET.get('username')
    user = User.objects.get(username=username)
    return JsonResponse({
        'success': True,
        'message': f'成功请求用户{username}的信息',
        'userinfo': {
            'username': username, 
            'avatar': user.avatar,
            'email': user.email,
            'signature': user.signature
        }
    })

def userslist(request):
    print('enter userslist')
    data = json.loads(request.body)
    pageNumber = data.get('pageNumber')
    number = data.get('number')
    records = User.objects.all().order_by('-user_id')[number * (pageNumber - 1): number * pageNumber]
    #print("number:", number)
    #print(records)
    data = serialize('json', records)
    #print(data)
    json_data = json.loads(data)
    # 提取每个对象中的 "fields" 字段
    fields_list = []
    for obj in json_data:
        fields_list.append(obj['fields'])
    # data = serialize('array', records)
    count = User.objects.count()
    #print("count:", count)
    return JsonResponse({
        'success': True,
        'total_users': count,
        'users': fields_list
    })
