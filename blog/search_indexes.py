from haystack import indexes


from .models import Article # 指定对于某个类的某些数据建立索引

class PostIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    # # 进行索引字段
    # title = indexes.CharField(model_attr='title')
    # body = indexes.CharField(model_attr='body')


    def get_model(self):
        return Article # 搜索的模型类

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
