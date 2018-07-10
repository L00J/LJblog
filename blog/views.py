from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from blog.models import Article,Category,Tag
from tutorial.models import Tutorial,Part

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #分页

import markdown





def index(request):

    """
    博客首页
    :param request:
    :return:
    """
    article_list = Article.objects.order_by('-publish')[:5] #最近5篇文章

    tutorial_list = Tutorial.objects.all() # 教程列表

    front_list = Article.objects.filter(category__name__contains="前端设计").order_by('-publish')[:5]
    web_list = Article.objects.filter(category__name__contains="Web开发").order_by('-publish')[:5]
    db_list = Article.objects.filter(category__name__contains="数据存储").order_by('-publish')[:5]

    go_list = Article.objects.filter(category__name__contains="Go").order_by('-publish')[:5]
    python_list = Article.objects.filter(category__name__contains="Python").order_by('-publish')[:5]

    ops_list = Article.objects.filter(category__name__contains="Ops").order_by('-publish')[:5]
    sec_list = Article.objects.filter(category__name__contains="安全").order_by('-publish')[:5]


    #return render(request, 'index.html', {"article_list": article_list,
    #              "tutorial_list" : tutorial_list,
    #              "front_list" : front_list })





    #Tutorial1 = Part.objects.filter(tutorial=Tutorial.objects.get(name="blog"))

    return render(request, 'index.html', locals())




def detail(request, pk):
    """
    博文详情
    """
    article = get_object_or_404(Article, pk=pk)
    article.viewed()#阅读量统计

    article.body = markdown.markdown(article.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    return render(request, 'detail.html', {"article": article,
                                             "source_id": article.id})




def archive(request):
    """
    文章归档
    """
    article_list = Article.objects.order_by('-publish')
    return render(request, 'archive.html', {"article_list": article_list})




def articles(request, pk):
    """
    博客列表页面
    :param request:
    :param pk:
    :return:
    """
    pk = int(pk)
    if pk:
        category_object = get_object_or_404(Category, pk=pk)
        category = category_object.name
        article_list = Article.objects.filter(category_id=pk)
    else:
        # pk为0时表示全部
        article_list = Article.objects.all()  # 获取全部文章
        category = ''
    return render(request, 'articles.html', {"article_list": article_list,
                                                  "category": category,
                                                  })