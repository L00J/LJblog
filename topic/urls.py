
from django.urls import path, re_path, include
# re_path方法相当于 django1.11 url正则表达式
from . import views
# from . import custom_search

# 载入视图模块

from haystack.views import SearchView

app_name = 'topic'
# 设置应用命名空间

urlpatterns = [

    re_path('(?P<pk>\d+)/$', views.topic, name='part'),

    # path('', views.index, name="index"),
    # path('topic', views.IndexView.as_view(), name="index"),
    #
    #
    # # re_path(r'^detail/(?P<pk>\d+)/$', views.detail, name='detail'),
    # re_path(r'^/topics/detail/(?P<pk>\d+).html$', views.detail, name='detail'),
    ]