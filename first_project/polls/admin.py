from django.contrib import admin

# Register your models here.

from .models import Question,Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice  #模型是Choice
    extra = 3       #一个Question添加3个选项


class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_data','question_text']
    # 字段分组+HTML样式
    fieldsets = [
        (None,{'fields':['question_text']}),
        ('发布时间', {'fields': ['pub_data'],'classes':['collapse']})
    ]

    list_display = ('question_text','pub_data')

    inlines = [ChoiceInline]

#注册自己的应用
# admin.site.register(Choice)
admin.site.register(Question,QuestionAdmin)