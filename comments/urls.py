from django.conf.urls import re_path

from . import views

app_name = 'comments'
urlpatterns = [
    re_path(r'^comment/article/(?P<pk>\d+)/$', views.article_comment, name='article_comment'),
]

