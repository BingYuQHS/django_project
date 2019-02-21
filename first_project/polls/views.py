from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import HttpResponse,Http404
from .models import Question,Choice

def index(request):
    question_list = Question.objects.all()
    context = {'question_list':question_list}

    return render(request,'polls/index.html',context)

def detail(request,question_id):
    #django中返回404错误页面的一种方法:Question是要查询的model,后面的pk＝id是查询条件
    question = get_object_or_404(Question,pk=question_id)
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404
    return render(request,'polls/detail.html',{'question':question})

def results(request,question_id):
    response = "你正在浏览问题【%s】的结果"
    return HttpResponse(response % question_id)

def vote(request,question_id):
    return HttpResponse("你正在为问题【%s】投票" % question_id)