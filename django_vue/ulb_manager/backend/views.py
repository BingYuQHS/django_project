from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
from . models import Book
from django.views.decorators.http import require_http_methods
import json
from django.core import serializers

# Create your views here.


def index(request):
    print('HttpRequest.scheme:', request.scheme)
    return HttpResponse('首页...')


#   add_book接受一个get请求，往数据库里添加一条book数据
@require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# show_books返回所有的书籍列表
# 通过JsonResponse返回能被前端识别的json格式数据
@require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list']  = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)