from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404

from blog.models import Article, Category, Tag

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 分页

import markdown

from django.views.generic import ListView, DetailView
from django.utils.safestring import mark_safe

from django.db.models import Q

from comments.forms import CommentForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# 分页模块


from django.core.paginator import Paginator
from django.views import View


def search(request):
    if request.user.is_authenticated:
        user_login = True

    key = request.GET.get('key')
    error_msg = ''

    tag_all = [tag for tag in Tag.objects.all()]

    if not key:
        error_msg = "请输入关键词"
        return render(request, 'index.html', {'error_msg': error_msg})

    elif request.user.is_authenticated:  # 判断是否登录
        article_list = Article.objects.filter(title__icontains=key)
        return render(request, 'index.html', {'error_msg': error_msg,
                                              "tag_all": tag_all,
                                              "user_login": user_login,
                                              "article_list": article_list, "key": key})
    else:
        error_msg = mark_safe('''<div class="alert alert-info">
				 <button type="button" class="close" data-dismiss="alert">×</button>
				<h4>
					提示!
				</h4> <strong>搜索失败!</strong> 请先登录 ...
			</div>''')
        return render(request, 'index.html', {'error_msg': error_msg})

    # article_list = Article.objects.filter(Q(title__icontains=key) | Q(body__icontains=key))
    # 全文搜索


class IndexView(View):
    """
    cbv 基于类视图
    """
    def get(self, request):

        post_all = Article.objects.all()  # 博客所有
        page = Paginator(post_all, 5)  # 将文章数分页(2)

        page_num = page.num_pages  # 分页数总数
        page_range = page.page_range  # 页码的列表数目

        page_first = page.page(1)  # 第1页的page对象
        # page_first_list = page_first.object_list  # 首页展示文章条数


        page_count = page.count  # 总数据量

        try:
            # GET请求方式，get()获取指定Key值所对应的value值
            # 获取page的值，url内输入的?page = 页码数  显示你输入的页面数目 默认为第1页
            num = request.GET.get('page', 1)
            # 获取第几页
            number = page.page(1)
        except PageNotAnInteger:
            # 如果输入的页码数不是整数，那么显示第一页数据
            number = page.page(1)
        except EmptyPage:
            number = page.page(page.num_pages)

        start = int(num)  # 当前页面数

        if page_num   > 5: # 总分页数大于5
            if start +5 > page_num:  # 你输入的值
                pageRange = range(start-4, start+1) # 大于展示按钮数量时

            else:
                pageRange = range(start, start+5)  # 显示分页按钮数量

        else:
            pageRange = page.page_range # 正常分配range(1, 4)


        currentPage = page.page(num)  # 当前页面

        currentRange = currentPage.number+1 # #显示末尾



        article_list = currentPage.object_list

        tag_all = [tag for tag in Tag.objects.all()]  # tags

        if request.user.is_authenticated:  # 登录
            user_login = True

        return render(request, 'index.html', locals())




def detail(request, pk):
    """
    博文详情
    """
    article = get_object_or_404(Article, pk=pk)
    ua = request.META.get('HTTP_USER_AGENT')
    ipaddr = request.META['REMOTE_ADDR']

    article.viewed()  # 阅读量统计

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    # 记得在顶部导入 CommentForm
    form = CommentForm()
    # 获取这篇 post 下的全部评论
    comment_list = article.comment_set.all()

    article.body = md.convert(article.body.replace("\r\n", '  \n'))
    toc = md.toc

    detail_tag = Article.objects.get(pk=pk).tags.all()

    if request.user.is_authenticated:
        user_login = True

    # context = {"article": article,
    #            'form': form,
    #            "ua":ua,
    #            "ipaddr":ipaddr,
    #            'comment_list': comment_list,
    #            "source_id": article.id,
    #            'toc': md.toc }

    context = locals()
    return render(request, 'detail.html', context)

    # context = {'article':article}
    # return  render(request,'detail.html',context)

    # article.content = markdown.markdown(article.content.replace("\r\n", '  \n'),extensions=[
    #                                  'markdown.extensions.extra',
    #                                  'markdown.extensions.codehilite',
    #                                  'markdown.extensions.toc',
    #                               ],safe_mode=True,enable_attributes=False)


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
    article_list = Article.objects.filter(publish__year=year, publish__month=month).order_by('-publish')
    return render(request, 'archive.html', context={"article_list": article_list})


class TagView(View):
    model = Tag
    context_object_name = 'tags'
    template_name = 'tags.html'


class CategoryView(View):
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
                                          "tag_all": tag_all
                                          })


def category(request, pk):
    # 记得在开始部分导入 Category 类

    if request.user.is_authenticated:
        user_login = True

    tag_all = [tag for tag in Tag.objects.all()]

    cate = get_object_or_404(Category, pk=pk)
    post_all = Article.objects.filter(category=cate).order_by('-publish')


    page = Paginator(post_all, 9)  # 将文章数分页(2)

    page_num = page.num_pages  # 分页数总数
    page_range = page.page_range  # 页码的列表数目

    page_first = page.page(1)  # 第1页的page对象
    # page_first_list = page_first.object_list  # 首页展示文章条数

    page_count = page.count  # 总数据量

    try:
        # GET请求方式，get()获取指定Key值所对应的value值
        # 获取page的值，url内输入的?page = 页码数  显示你输入的页面数目 默认为第1页
        num = request.GET.get('page', 1)
        # 获取第几页
        number = page.page(1)
    except PageNotAnInteger:
        # 如果输入的页码数不是整数，那么显示第一页数据
        number = page.page(1)
    except EmptyPage:
        number = page.page(page.num_pages)

    start = int(num)  # 当前页面数

    if page_num > 5:  # 总分页数大于5
        if start + 5 > page_num:  # 你输入的值
            pageRange = range(start - 5, start)

        else:
            pageRange = range(start, start + 5)  # 显示分页按钮数量

    else:
        pageRange = page.page_range  # 正常分配range(1, 4)


    currentPage = page.page(num)  # 当前页面
    article_list = currentPage.object_list

    return render(request, 'category.html', context=locals())