
from django.db import models
from django.utils import timezone


# Create your models here.
from django.shortcuts import reverse
from mdeditor.fields import MDTextField #


#
class Topic(models.Model):
    name = models.CharField(max_length=128, verbose_name="专题名")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "专题分类"
        verbose_name_plural = "专题分类"


# 文章
class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name="文章名称")
    body = MDTextField(verbose_name='正文', blank=True, null=True)
    #body = models.TextField(verbose_name="正文")
    topic = models.ForeignKey("Topic",  on_delete=models.CASCADE,verbose_name="所属专题")
    visiting = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name="访问量")
    parent = models.ForeignKey("self", blank=True, default=None, null=True, related_name="child_post", on_delete=models.CASCADE,                              verbose_name="父亲文章")
    prev_post = models.OneToOneField("self", default=None, blank=True, null=True, related_name="next_post",
                                     on_delete=models.CASCADE,verbose_name="前一篇文章")
    ctime = models.DateTimeField(verbose_name='发布时间', default=timezone.now)  # 发布时间
    # ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    level = models.PositiveSmallIntegerField(blank=True, null=True, default=None)

    def __str__(self):
        return self.topic.name + "......" + self.title

    def increase_views(self):
        self.visiting += 1
        self.save(update_fields=['visiting'])

    def save(self, *args, **kwargs):

        if not self.parent:
            self.level = 0
        else:
            self.level = self.parent.level + 1
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'Topic':self.Topic.name,'post_id': self.id})

    class Meta:
        verbose_name = "专题文章"
        verbose_name_plural = "专题文章"
        ordering = ["ctime"]