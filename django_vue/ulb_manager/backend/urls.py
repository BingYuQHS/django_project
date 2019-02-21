from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'add_book$', views.add_book, name='add_book'),
    url(r'show_books$', views.show_books, name='show_books'),
]