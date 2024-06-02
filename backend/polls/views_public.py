from django.http import JsonResponse
import json
from .models import *
from django.core.serializers import serialize

# 表白墙按钮接口，显示所有publicpost
def publicpost(request):
    print('enter publicbox')
    records = publicpost.objects.all().order_by('-public_id')
    records = serialize('json', records)
    json_data = json.loads(records)
    fields_list = []
    for obj in json_data:
        fields_list.append(obj['fields'])
    updated_data = []
    for item in updated_data:
        # public_id = item.get('public_id')
        head_thread = item.get('head_thread')
        thethread = publicthread.objects.get(publicthread_id=head_thread)
        description = thethread.content
        is_anonymous = thethread.is_anonymous
        user_id = thethread.user_id_thread_id
        user = User.objects.get(user_id=user_id)
        username = user.username
        avatar = user.avatar
        updated_item = {
            'username': username,
            'avatar': avatar,
            'is_anonymous': is_anonymous,
            # 如果匿名，那么username和头像应该隐藏，这应该是前端实现的？
            'description': description,
            # 第一个人的content，类似于发帖人的标题，类比box所以取名叫description，也可以改名
        }
        updated_data.append(updated_item)
    count = publicpost.objects.count()
    return JsonResponse({
        'success': True,
        'posts': updated_data,
        'totalposts': count,
    })
    # 这里我不知道你前端接口的名字是什么，我大概按照之前box和getpost等接口的格式模仿了一下，具体你可以改qaq

def appendpublicpost(request):
    print('enter appendpublicpost')
    ## 这里假设你使用的是post方法
    data = json.loads(request.body)
    username = data.get('username')
    content = data.get('content')
    is_anonymous = data.get('is_anonymous')
    user_id = User.objects.get(username=username)
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