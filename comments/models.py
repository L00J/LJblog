from django.db import models

# Create your models here.



from django.db import models
from django.utils.six import python_2_unicode_compatible

# python_2_unicode_compatible 装饰器用于兼容 Python2
@python_2_unicode_compatible
class Comment(models.Model):
    name = models.CharField('评论用户', max_length=50)
    email = models.EmailField('邮箱',max_length=255)
    url = models.URLField('站点', max_length=100,blank=True,)
    text = models.TextField('评论内容', max_length=500)
    created_time = models.DateTimeField('评论时间',auto_now_add=True)

    article = models.ForeignKey('blog.Article',on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]

    def commenced(self):
        """
        增加评论数
        :return:
        """
        self.comment += 1
        self.save(update_fields=['comment'])


