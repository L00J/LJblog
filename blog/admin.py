from django.contrib import admin



from.models import Article,Category,Tag

from tutorial.models import Tutorial,Part

class Articleslist(admin.ModelAdmin):
    list_display = ['title','publish','mod_date','category','author']
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