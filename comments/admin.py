from django.contrib import admin

# Register your models here.

from .models import Comment




# 评论
class Commentlist(admin.ModelAdmin):
    list_display = ['name', 'url', 'article','email','created_time']  # 分类


admin.site.register(Comment,Commentlist)


