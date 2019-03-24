from django.shortcuts import render,redirect
from .models import * # 载入应用数据

# Create your views here.
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger # 分页

from haystack.views import SearchView # haystack视图
from django.utils.safestring import mark_safe # html样式




#搜索引擎 全站搜索
class MySearchIndex(SearchView):

    template = 'search/search.html'
    #我们通过重写extra_context 来定义我们自己的变量，
    #通过看源码，extra_context 默认返回的是空，然后再get_context方法里面，把extra_context
    #返回的内容加到我们self.context字典里
    def extra_context(self):
        context = super(MySearchIndex,self).extra_context()
        # search_Article = Article.objects.select_related('body').order_by('-dynamic_search').all()[:6]

        # tag_all = [tag for tag in Tag.objects.all()]  # 添加博客自定义tags

        if self.request.user.is_authenticated:  # 认证
            user_login = True

        if not self.request.GET.get('q'):

            error_msg = "请输入关键词"
            context =  {'error_msg': error_msg}



        elif self.request.user.is_authenticated:
            context = locals()


        else:
            error_msg = mark_safe('''<div class="alert alert-info">
            				 <button type="button" class="close" data-dismiss="alert">×</button>
            				<h4>
            					提示!
            				</h4> <strong>搜索失败!</strong> 请先登录 ...
            			</div>''')
            context = {'error_msg': error_msg}
        return  context






    # def create_response(self):
    #
    #     if not self.request.GET.get('q'):
    #         print(self.request.GET.get('q'))
    #
    #         # search_Article = Article.objects.select_related('body').order_by('-dynamic_search').all()[:6]
    #         article_info = Article.objects.all()
    #
    #         paginator = Paginator(article_info, settings.HAYSTACK_SEARCH_RESULTS_PER_PAGE)
    #
    #
    #         try: # 分页
    #             page = paginator.page(int(self.request.GET.get('page',1)))
    #         except PageNotAnInteger:
    #             page = paginator.page(1)
    #         except EmptyPage:
    #             page = paginator.page(paginator.num_pages)
    #         print(page)
    #         return render(self.request, self.template, locals())
    #     else:
    #         qs = super(MySearchIndex, self).create_response()
    #        # print(self.get_context())
    #         return qs
