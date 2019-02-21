from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField('姓名',max_length=20)
    age = models.IntegerField('年龄')

    def __str__(self):
        return self.name

# 博客
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

# 作者
class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

# 具体的一篇博客（该文章是那个blog的文章，标题、内容、发布、修改、作者、评论数、回复数、评分）
class Entry(models.Model):
    blog = models.ForeignKey('Blog',on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline