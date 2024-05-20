from django.http import JsonResponse
import json
from .models import *
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder

def delete_box(host_id):
    try:
        box_old = Box.objects.get(host_id=host_id)
        box_old.delete()
        print('box deleted')
    except Box.DoesNotExist:
        print('box not found')

def share(request):
    print('enter share')
    data = json.loads(request.body)
    username = data.get('username')
    description = data.get('description')
    host_id = User.objects.get(username=username).user_id
    delete_box(host_id)
    box_new = Box(descr=description, host_id=host_id)
    box_new.save()
    return JsonResponse({
        'success': True,

    })

def box(request):
    print('enter box')
    records = Box.objects.all().order_by('-box_id')
    records = serialize('json', records)
    json_data = json.loads(records)
    #print(json_data)
    fields_list = []
    for obj in json_data:
        fields_list.append(obj['fields'])
    updated_data = []
    for item in fields_list:
        host_id = item.get('host')
        try:
            user = User.objects.get(user_id=host_id)
            username = user.username
        except User.DoesNotExist:
            username = None
        updated_item = {
            'username': username,
            'description': item.get('descr')
        }
        updated_data.append(updated_item)
    count = Box.objects.count()
    return JsonResponse({
        'success': True,
        'boxes': updated_data,
        'total_boxes': count
    })

def post(request):
    print('enter post')
    data = json.loads(request.body)
    username = data.get('username')
    hostUsername = data.get('hostUsername')
    question = data.get('question')
    try:
        poster = User.objects.get(username=username)
        poster_id = poster.user_id
    except User.DoesNotExist:
        poster_id = None
    try:
        host = User.objects.get(username=hostUsername)
        host_id = host.user_id
    except User.DoesNotExist:
        host_id = None
    post_new = Post(question=question, is_public=True, host_id=host_id, poster_id=poster_id)
    post_new.save()
    return JsonResponse({
        'success': True
    })

def gethostpost(request):
    print('enter gethostpost')
    username = request.GET.get('username', None)
    host_id = User.objects.get(username=username).user_id
    print(host_id)
    posts = Post.objects.get(host_id=host_id).order_by('-post_id')
    # posts = Post.objects.filter(host_id=host_id).order_by('-post_id')
    print(posts)
    # posts_list = list(posts.values())
    # posts_json = json.dumps(posts_list, cls=DjangoJSONEncoder)
    # print(posts_json)
    # updated_data = []
    # for item in posts_json:
    #     updated_item = {
    #         'id': item.get('post_id'),
    #         'username': username,
    #         'question': item.get('question'),
    #         'answer': item.get('answer'),
    #         'is_public': item.get('is_public')
    #     }
    #     updated_data.append(updated_item)
    # print(posts_json)
    # count = Post.objects.filter(host_id=host_id).count()
    # return JsonResponse({
    #     'success': True,
    #     'posts': posts_json,
    #     'total_posts': count
    # })