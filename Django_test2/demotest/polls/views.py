from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import random
# Create your views here.

def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    u = request.POST.get('user', '')
    p = request.POST.get('pwd', '')
    if u and p:
        find_user = StudentInfo.objects.filter(stu_name=u, stu_pwd=p).count()
        if find_user:
            return HttpResponse('登陆成功')
        else:
            return HttpResponse('账号或密码错误！')
        # return HttpResponse('输入正确')
    else:
        return HttpResponse('请输入正确的账号和密码')

#渲染注册界面
def toregister_view(request):
    return render(request, 'register.html')
def register_view(request):
    u = request.POST.get('user', '')
    p = request.POST.get('pwd', '')
    if u and p:
        stu = StudentInfo(stu_id=str(random.randrange(1111, 9999)), stu_name=u, stu_pwd=p)
        stu.save()
        return HttpResponse('注册成功~')
    else:
        return HttpResponse('请输入完整的账号和密码！')