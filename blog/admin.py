from django.contrib import admin



from .models import Article,Category,Tag

from tutorial.models import Tutorial,Part

class Articleslist(admin.ModelAdmin):
    list_display = ['title','category','mod_date','author']
    list_filter = ['publish','category']
    search_fields = ['title']
    #display 展示表字段，filter过滤分类，search搜索内容

    #重写ModelAdmin模块的save_model方法
    def save_model(self, request, obj, form, change):
        if not obj.id:
            obj.author = request.user.username
        obj.save()

class TutorialList(admin.ModelAdmin):
    list_display = ['title','publish','mod_date','tutorial','view']




admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article,Articleslist)

admin.site.register(Tutorial)
admin.site.register(Part,TutorialList)