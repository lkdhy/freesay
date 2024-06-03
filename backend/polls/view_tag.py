from django.http import JsonResponse
from . models import Tag

def gettags(request):
    # print('enter gettags')
    # print(list(Tag.objects.all().values_list('tag_name', flat=True)))
    return JsonResponse({
        'success': True,
        'message': '成功请求当前存下的所有标签',
        'tags': list(Tag.objects.all().values_list('tag_name', flat=True))
    })