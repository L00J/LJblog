#!/usr/bin/env python
# -*- coding: utf-8 -*-
# --------------------------------------------------
# Author:    LJ
# Email:     admin@attacker.club

# Date:      18-5-29
# Description:
# --------------------------------------------------


from django.urls import path, re_path
# re_path方法相当于 django1.11 url正则表达式
from . import views
#载入视图模块




app_name = 'blog'
#设置应用命名空间

urlpatterns = [
    path('', views.index, name="index"),

    # r正则;（）取出的内容;?P<> 里面是视图的参数名;[0-9]+数字;$结尾
    #re_path(r'^(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    #re_path(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),

    # re_path(r'^detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    re_path(r'^detail/(?P<pk>\d+).html$', views.detail, name='detail'),
    #re_path(r'^archive/$', views.archive, name='archive'),
    re_path(r'^articles/$', views.archive, name='articles'),
    #re_path(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archive, name='archive'),
    path('archive/<int:year>/<int:month>/', views.archive, name='archive'),  # http://127.0.0.1:8000/archive/2019/1/



    re_path(r'^tag/$', views.TagView.as_view(), name='tag'),
    re_path(r'^category/$', views.CategoryView.as_view(), name='category'),
    re_path(r'^archive/$', views.ArchiveView.as_view(), name='archive'),
    re_path(r'^search/$', views.search, name='search'),


    re_path(r'^tag/(?P<name>.*?)/$', views.tag, name='tag'),
    re_path(r'^category/(?P<pk>\d+)/$', views.category, name='category'),


  
    # ex: /polls/5/
    # ex: /polls/5/results/
    # ex: /polls/5/vote/
]
