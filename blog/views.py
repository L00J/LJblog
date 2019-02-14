from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from blog.models import Article,Category,Tag

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger #分页

import markdown

from django.views.generic import ListView, DetailView


from django.db.models import Q

from comments.forms import CommentForm


def search(request):
    key = request.GET.get('key')
    error_msg = ''

    tag_all = [tag for tag in Tag.objects.all()]

    if not key:
        error_msg = "请输入关键词"
        return render(request, 'index.html', {'error_msg': error_msg})

    # article_list = Article.objects.filter(Q(title__icontains=key) | Q(body__icontains=key))
    # 全文搜索
    article_list = Article.objects.filter(title__icontains=key)
    return render(request, 'index.html', {'error_msg': error_msg,
                                          "tag_all" : tag_all,
                                               "article_list": article_list, "key": key})


def index(request):

    """
    博客首页
    :param request:
    :return:
    """
    article_list = Article.objects.order_by('-publish')[:5] #最近5篇文章


    front_list = Article.objects.filter(category__name__contains="前端设计").order_by('-publish')[:5]
    web_list = Article.objects.filter(category__name__contains="Web开发").order_by('-publish')[:5]
    db_list = Article.objects.filter(category__name__contains="数据存储").order_by('-publish')[:5]

    go_list = Article.objects.filter(category__name__contains="Go").order_by('-publish')[:5]
    python_list = Article.objects.filter(category__name__contains="Python").order_by('-publish')[:5]

    ops_list = Article.objects.filter(category__name__contains="Ops").order_by('-publish')[:5]
    sec_list = Article.objects.filter(category__name__contains="安全").order_by('-publish')[:5]

    tag_all =  [tag for tag in Tag.objects.all()]

    return render(request, 'index.html', locals())




def detail(request, pk):
    """
    博文详情
    """
    article = get_object_or_404(Article, pk=pk)
    article.viewed()#阅读量统计

    ua = request.META.get('HTTP_USER_AGENT')





    # article.body = markdown.markdown(article.body.replace("\r\n", '  \n'),
    # # article.body = markdown.markdown(article.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra',
    #                                   'markdown.extensions.codehilite',
    #                                   'markdown.extensions.toc',
    #                               ],safe_mode=True,enable_attributes=False)
    # return render(request, 'detail.html', {"article": article,
    #                                        "source_id": article.id,
    #              } )

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = article.comment_set.all()

    article.body = md.convert(article.body.replace("\r\n",'  \n'))
    return render(request, 'detail.html', {"article": article,
                                           'form': form,
                                           "ua":ua,
                                           'comment_list': comment_list,
                                           "source_id": article.id,
                                           'toc': md.toc })





    # context = {'article':article}
    # return  render(request,'detail.html',context)

    # article.content = markdown.markdown(article.content.replace("\r\n", '  \n'),extensions=[
    #                                  'markdown.extensions.extra',
    #                                  'markdown.extensions.codehilite',
    #                                  'markdown.extensions.toc',
    #                               ],safe_mode=True,enable_attributes=False)




# def archive(request):
#     """
#     文章归档
#     """
#     article_list = Article.objects.order_by('-publish')
#     return render(request, 'archive.html', {"article_list": article_list})
#





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



def archive(request, year, month):
    """
    归档
    :param request:
    :param year:
    :param month:
    :return:
    """
    article_list = Article.objects.filter(publish__year=year,publish__month=month).order_by('-publish')
    return render(request, 'archive.html', context={"article_list": article_list})







class TagView(ListView):
    model = Tag
    context_object_name = 'tags'
    template_name = 'tags.html'


class CategoryView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'category.html'


class ArchiveView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'archive.html'


def tag(request, name):
    """
    标签
    :param request:
    :param name
    :return:
    """

    tag_all = [tag for tag in Tag.objects.all()]

    article_list = Article.objects.filter(tags__name=name)
    return render(request, 'index.html', {"article_list": article_list,
                                          "tag_all":tag_all
                                          })

def category(request, pk):
    # 记得在开始部分导入 Category 类

    tag_all = [tag for tag in Tag.objects.all()]

    cate = get_object_or_404(Category, pk=pk)
    article_list = Article.objects.filter(category=cate).order_by('-publish')
    return render(request, 'index.html', context={'article_list': article_list,
                                                  "tag_all":tag_all,
                                                  })




