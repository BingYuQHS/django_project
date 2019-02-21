from django.conf.urls import url
#从当前目录导入views
from . import views
urlpatterns = [
    #ex：/pools/
    url(r'^$', views.index, name='index'),
    #ex：/pools/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    #ex：/pools/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    #ex：/pools/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]