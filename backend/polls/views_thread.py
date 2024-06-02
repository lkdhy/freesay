from django.http import JsonResponse
import json
from . models import Post, Thread

def get_thread(head):
    # if head:
    #     print('in get_thread:', head)
    nxt = head
    thread = []
    while nxt:
        message = Thread.objects.get(thread_id=nxt)
        thread.append(message.content)
        nxt = message.nxt
    # if head:
        # print(thread)
    return thread
    
def appendthread(request):
    data = json.loads(request.body)
    pid = data.get('id')
    content = data.get('content')
    new_thread_id = Thread.objects.create(content=content).thread_id
    post = Post.objects.get(post_id=pid)
    tid = post.head_thread
    if tid == 0:
        post.head_thread = new_thread_id
        post.save()
        return JsonResponse({
            'success': True,
            'message': '之前没有thread，成功创建头部thread消息',
        })
    while 1:
        message = Thread.objects.get(thread_id=tid)
        if (message.nxt):
            tid = message.nxt
        else:
            message.nxt = new_thread_id
            message.save()
            break
    return JsonResponse({
        'success': True,
        'message': '已有thread，成功创建将消息接到thread最后',
    })