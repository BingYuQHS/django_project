from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField('问题',max_length=50)
    pub_data = models.DateTimeField('发布时间')

    def __str__(self):
        return self.question_text

    #这个类让类对象显示一个中文提示（Question=>问题）
    class Meta:
        verbose_name = ('问题')
        verbose_name_plural = verbose_name



class Choice(models.Model):
    question = models.ForeignKey('Question',on_delete=models.CASCADE)
    choice_text = models.CharField(verbose_name="选项",max_length=200)
    votes = models.IntegerField(verbose_name="投票数", default=0)

    def __str__(self):
        return self.choice_text

    # 这个类让类对象显示一个中文提示（Choice=>选项）
    class Meta:
        verbose_name = ('选项')
        verbose_name_plural = verbose_name

