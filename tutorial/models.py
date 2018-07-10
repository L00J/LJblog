from django.db import models
from django.utils import timezone


class Tutorial(models.Model):  # 专题教程
    """
    继承django.db.models.Models模块
    """
    name = models.CharField(verbose_name='专题教程', max_length=100)

    def __str__(self):
        return self.name



class Part(models.Model):
    """
    文章的数据库表稍微复杂一点，主要是涉及的字段更多。
    django会自动新建自增id作为主键
    """
    title = models.CharField(verbose_name='标题', max_length=70)  # 标题
    body = models.TextField(verbose_name='正文', blank=True, null=True)  # 文章正文
    publish = models.DateTimeField(verbose_name='发布时间', default=timezone.now)  # 发布时间
    mod_date = models.DateField(verbose_name='更新时间', auto_now=True)  # 更新时间
    tutorial = models.ForeignKey(Tutorial, verbose_name='专题教程', on_delete=models.CASCADE)  # 教程
    view = models.BigIntegerField(verbose_name='阅读数', default=0)  # 阅读数

    def __str__(self):
        return self.title

    def viewed(self):
        """
        增加阅读数
        :return:
        """
        self.view += 1
        self.save(update_fields=['view'])
