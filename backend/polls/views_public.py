from django.http import JsonResponse
import json
from .models import *
from django.core.serializers import serialize

# 表白墙按钮接口，显示所有publicpost
def getpublicpost(request):
    print('enter publicbox')
    records = publicpost.objects.all().order_by('-public_id')
    records = serialize('json', records)
    json_data = json.loads(records)
    fields_list = []
    for obj in json_data:
        fields_list.append(obj['fields'])
    updated_data = []
    for item in fields_list:
        # public_id = item.get('public_id')
        tid = item.get('head_thread')
        cur = publicthread.objects.get(publicthread_id=tid)
        user_id = cur.user_id_thread_id

        user = User.objects.get(user_id=user_id)
        username = user.username # 链中第一个人的username
        avatar = user.avatar # 链中第一个人的头像

        is_anonymous = cur.is_anonymous # 链中第一个人是否匿名，这将影响是否在一点进去的表白墙界面中显示发帖者的头像和用户名

        # thread_name = []
        # thread_content = []
        # thread_anonymous = []
        thread = []
        while tid > 0: # 获取三个数组，thread链中的名字、内容和是否匿名
            cur = publicthread.objects.get(publicthread_id=tid)
            content = cur.content
            is_ano = cur.is_anonymous

            uid = cur.user_id_thread_id
            user = User.objects.get(user_id=uid)
            thread.append({
                'username': user.username,
                'avatar': user.avatar,
                'content': content,
                'is_anonymous': is_ano,
            })
            # thread_name.append(uname)
            # thread_content.append(content)
            # thread_anonymous.append(is_ano)
            tid = cur.nxt

        updated_item = {
            'username': username,
            'avatar': avatar,
            'is_anonymous': is_anonymous,
            'thread': thread,
            # 如果匿名，那么username和头像应该隐藏，这应该是前端实现的？
            # 'threadcontent': thread_content,
            # 'threadusername': thread_name,
            # 'threadanonymous': thread_anonymous,
        }
        updated_data.append(updated_item)
    print(updated_data)

    count = publicpost.objects.count()
    return JsonResponse({
        'success': True,
        'posts': updated_data,
        'totalposts': count,
    })
    # 这里我不知道你前端接口的名字是什么，我大概按照之前box和getpost等接口的格式模仿了一下，具体你可以改qaq

# A在表白墙了新增一个post
def addpublicpost(request):
    # post方法
    data = json.loads(request.body)
    #这里是username或者user_id都可以，看你怎么方便
    # ——用username
    username = data.get('username') 
    content = data.get('content')
    is_anonymous = data.get('is_anonymous')

    user_id = User.objects.get(username=username).user_id
    thread_new = publicthread.objects.create(
        content=content,
        nxt=0,
        is_anonymous=is_anonymous,
        user_id_thread_id=user_id,
    )
    publicthread_id = thread_new.publicthread_id

    post_new = publicpost.objects.create(
        head_thread=publicthread_id
    )
    return JsonResponse({
        'success': True,
        'message': '成功post表白墙'
    })

def appendpublicpost(request):
    print('enter appendpublicpost')
    data = json.loads(request.body)
    pid = data.get('id')
    content = data.get('content')
    is_anonymous = data.get('is_anonymous')
    username = data.get('username') #同上，也可以改成user_id，看你怎么方便了
    user_id = User.objects.get(username=username).user_id

    # 创立新的publicthread
    new_thread_id = publicthread.objects.create(
        content=content,
        nxt=0,
        is_anonymous=is_anonymous,
        user_id_thread_id=user_id,
    )

    post = publicpost.objects.get(publicpost_id=pid)
    tid = post.head_thread
    while tid > 0:
        cur = publicthread.objects.get(publicthread_id=tid)
        tid = cur.nxt
    cur.nxt = new_thread_id
    cur.save() # 保存新的cur，增加了nxt
    return JsonResponse({
        'success': True,
        'message': '创建表白墙thread',
    })

