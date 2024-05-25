from django.http import JsonResponse
import json
from .models import *
from django.core.serializers import serialize

def setsignature(request):
    print("enter setsignature")
    data = json.loads(request.body)
    username = data.get('username')
    signature = data.get('signature')
    User.objects.filter(username=username).update(signature=signature)


