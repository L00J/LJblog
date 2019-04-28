from django.shortcuts import render

# Create your views here.
from  .models import Post,Topic
from django.shortcuts import render, get_object_or_404

import markdown
from django.utils.safestring import mark_safe


def topic(request, pk):

    if request.user.is_authenticated:
        user_login = True


    topic_indexes = {}
    topic_all = Topic.objects.all()  # 专题
    for t in topic_all:
        k = [i.pk for i in Post.objects.filter(topic=t.pk)[:1]]
        if len(k) > 0:
            topic_indexes[k[0]] = t.name


    # t = get_object_or_404(Topic, pk=pk) # part
    # post_all = Post.objects.filter(topic=t).order_by('pk') # 专题下内容


    post = get_object_or_404(Post, pk=pk)

    post.increase_views() # 阅读量统计

    topic_index = Topic.objects.filter(post__pk=pk)
    topic_pk = [i for i in topic_index][0]

    post_all = Post.objects.filter(topic=topic_pk)

    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    post.body = md.convert(post.body.replace("\r\n", '  \n'))
    toc = md.toc



    return render(request, 'topic/post.html', context=locals())