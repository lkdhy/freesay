from django.http import JsonResponse
import json
from .models import *
from django.core.serializers import serialize

# sender发送私聊给某用户
def appendchat(request):
    # 前端传给我的信息：（你当然可以修改名字）
    # sender代表发消息的人的用户名
    # user1、user2代表当前聊天的两个人的用户名 顺序无所谓
    print("appendchat")
    # 先按照post方法接受
    data = json.loads(request.body)
    sender = data.get('sender')
    user1 = data.get('user1')
    user2 = data.get('user2')
    sender = User.objects.get(username=sender).user_id
    user1 = User.objects.get(username=user1).user_id
    user2 = User.objects.get(username=user2).user_id
    msg = data.get('content')
    if user1 > user2:
        user1, user2 = user2, user1
    chat.objects.create(sender=sender, message=msg, user1=user1, user2=user2)

def getchat(request):
    # 前端传给我的信息：
    # host代表当前登录用户的用户名
    # user1、user2代表当前聊天的两个人的用户名 顺序无所谓
    print("getchat")
    data = json.loads(request.body)
    host = data.get('host')
    user1 = data.get('user1')
    user2 = data.get('user2')
    if user1 > user2:
        user1, user2 = user2, user1
    chats = chat.objects.filter(user1=user1, user2=user2).order_by('chat_id')
    chat_list = list(chats.values())
    ret_list = []
    for item in chat_list:
        user1 = item.get('user1')
        user2 = item.get('user2')
        message = item.get('message')
        sender = item.get('sender')
        if user1 == sender:
            sendername = User.objects.get(user_id=user1).username
        else:
            sendername = User.objects.get(user_id=user2).username
        chat_dict = {
            'username': sendername,
            'message': message
        }
        ret_list.append(chat_dict)
    return JsonResponse({
        'success': True,
        'chats': ret_list,
        'total_chats': len(ret_list)
    })
    # 前端接受的：chats是一个list，里面每一个元素
    # 都是一个字典，username代表发某条信息的人，
    # message代表信息内容，已经按顺序排好