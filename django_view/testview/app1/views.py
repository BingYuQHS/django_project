from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.

def index(request):
    # HttpRequest.scheme: 一个字符串，表示请求的方案（通常是http或https）
    # HttpRequest.body: 一个字符串，表示原始Http请求的正文
    # HttpRequest.path：一个字符串，表示请求页面的完整路径，不包含域名
    # HttpRequest.path_info
    # HttpRequest.method：一个字符串，表示请求使用的HTTP方法，必须使用大写
    # HttpRequest.encoding
    # HttpRequest.GET：一个类似于字典的对象，包含HTTP GET的所有参数
    # HttpRequest.POST：一个包含所有给定的HTTP POST参数的类字典对象，提供了包含表单数据的请求
    # HttpRequest.COOKIES：一个标准的Python字典，包含所有的cookie，键和值都为字符串。
    # HttpRequest.FILES：一个类似于字典的对象，包含所有的上传文件。
    # HttpRequest.META：一个标准的Python字典，包含所有HTTP头部
    # HttpRequest.user
    # HttpRequest.session
    # HttpRequest.urlconf
    # HttpRequest.resolver_match
    print('HttpRequest.scheme:',request.scheme)

    return HttpResponse('首页...')
