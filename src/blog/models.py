
from django.db import models



# Create your models here.
#This is a database sheet.
class Article(models.Model):
    
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Published'),
                      )
    
    
    #field means a column of database.
    title = models.CharField('标题', max_length = 70)
    content = models.TextField('正文')
    #auto_now_add will auto create time
    created_time = models.DateTimeField('创建时间', auto_now_add = True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length = 54, blank = True, null = True,
                                help_text = '可选，如若为空将摘取正文的前54个字符')
    #how many times of viewing and likes
    views = models.PositiveIntegerField('浏览量', default = 0)
    likes = models.PositiveIntegerField('点赞数', default = 0)
    
    #top or not
    topped = models.BooleanField('置顶', default = False)
    # category: have a foreign key.
    #ForeignKey、ManyToManyField 和 OneToOneField 都要求第一个参数是一个模型类，所以要使用 verbose_name 关键字参数才能指定自述名：
    #当一个ForeignKey 引用的对象被删除时，Django 默认模拟SQL 的ON DELETE CASCADE 的约束行为，并且删除包含该ForeignKey的对象。
    #这种行为可以通过设置on_delete 参数来改变。例如，如果你有一个可以为空的ForeignKey，在其引用的对象被删除的时你想把这个ForeignKey 设置为空：
    #第一个参数对应的是下面的这个表
    category = models.ForeignKey('Category', verbose_name='分类',
                                 null = True,
                                 blank=True,
                                 on_delete = models.SET_NULL
                                 )
   
    def __str__(self):
        # 主要用于交互解释器显示表示该类的字符串
        return self.title
    class Meta:
        # Meta 包含一系列选项，这里的 ordering 表示排序，- 号表示逆序。即当从数据库中取出文章        
        # 时，其是按文章最后一次修改时间逆序排列的。
        ordering = ['-last_modified_time']



#This is another database sheet:这个是外键进入的表
class Category(models.Model):

    name = models.CharField('类名', max_length = 20)
    created_time = models.DateTimeField('创建时间', auto_now_add = True)
    last_modified_time = models.DateTimeField('修改时间', auto_now = True)
    
    def __str__(self):
        # 主要用于交互解释器显示表示该类的字符串
        return self.name
