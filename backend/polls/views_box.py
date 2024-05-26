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
            signature = user.signature
        except User.DoesNotExist:
            username = None
        updated_item = {
            'username': username,
            'hostSignature': signature,
            'description': item.get('descr')
        }
        updated_data.append(updated_item)
    count = Box.objects.count()
    return JsonResponse({
        'success': True,
        'message': '成功请求所有分享广场的提问箱',
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
    ## add; haven't test

    post_id = post_new.post_id #不知道对不对
    ## post_id = Post.objects.filter(question=question).post_id
    tags = data.get('tags')
    for tag in tags:
        find_tag = Tag.objects.filter(tag_name=tag).count()
        if find_tag == 0:
            Tag(tag_name=tag).save()
        tag_id = Tag.objects.filter(tag_name=tag).tag_id
        with_tag = with_tag(post_id_with_id=post_id, tag_id_with_id=tag_id)
        with_tag.save()

    ##
    return JsonResponse({
        'success': True,
        'message': '成功post问题及标签（若有）'
    })

def gethostpost(request):
    print('enter gethostpost')
    username = request.GET.get('username', None)
    host_id = User.objects.get(username=username).user_id
    posts = Post.objects.filter(host_id=host_id).order_by('-post_id')
    posts_list = list(posts.values())
    # posts_json = json.dumps(posts_list, cls=DjangoJSONEncoder)
    # print(posts_json)
    updated_data = []
    for item in posts_list:
        updated_item = {
            'id': item.get('post_id'),
            'username': username,
            'question': item.get('question'),
            'answer': item.get('answer'),
            'is_anonymous': item.get('is_anonymous'),
            'is_public': item.get('is_public')
        }
        updated_data.append(updated_item)
    #print(updated_data)
    count = Post.objects.filter(host_id=host_id).count()
    #print(count)
    return JsonResponse({
        'success': True,
        'posts': updated_data,
        'total_posts': count
    })

def getpost(request):
    print('enter getpost')
    username = request.GET.get('username', None)
    poster_id = User.objects.get(username=username).user_id
    posts = Post.objects.filter(poster_id=poster_id).order_by('-post_id')
    posts_list = list(posts.values())
    #print(posts_list)
    updated_data = []
    for item in posts_list:
        hostname = User.objects.get(user_id = item.get('host_id')).username
        updated_item = {
            'id': item.get('post_id'),
            'username': hostname, ##???
            'question': item.get('question'),
            'answer': item.get('answer'),
            'is_public': item.get('is_public')
        }
        updated_data.append(updated_item)
    count = Post.objects.filter(poster_id=poster_id).count()
    #print(updated_data)
    #print(count)
    return JsonResponse({
        'success': True,
        'posts': updated_data,
        'total_posts': count
    })

def answer(request):
    print('enter answer')
    data = json.loads(request.body)
    post_id = data.get('id')
    answer = data.get('answer')
    is_public = data.get('is_public')
    if post:
        Post.objects.filter(post_id=post_id).update(answer=answer, is_public=is_public)
        return JsonResponse({
            'success': True,
            'message': "收到回答并保存成功"
        })
    else:
        return JsonResponse({
            'success': False,
            'message': '未找到post'
        })