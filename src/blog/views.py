
from django.views.generic import ListView
import markdown2

from blog.models import Category, Article
from django.views.generic.detail import DetailView
from blog.models import Article

# Create your views here.
#首页视图，用于展示从数据库中获取的文章列表
class IndexView(ListView):
    template_name = "article_list.html" #template_name用于指定使用哪个模板进行渲染:之前是blog/article_list.html,我还是决定把templates中的blog文件夹给删了
                                        #因为setting中的templates的path是不好动态获取的TnT。
                    #其中base是父类，article_list是继承自base.html的，在加载的时候，先加载子类，子类发现有继承父类之后，加载父类
                    #以下是其工作方式。 在加载 current_datetime.html 模板时，模板引擎发现了 {% extends %} 标签， 注意到该模板是一个子模板。 模板引擎立即装载其父模板，即本例中的 base.html 。
                    
                             
    context_object_name = "article_list" # context_object_name属性用于给上下文变量取名（在模板article_list中的上下文变量使用该名字）
    
    def get_queryset(self):
        '''
                    过滤数据，获取所有已经发布文章，并将内容转换为markdown形式
        '''
        #这里的article_lists与上面那个上下文article_list没什么关系！！！
        article_lists = Article.objects.filter(status = 'p')
        #for article in article_lists:
        #    article.content = markdown2.markdown(article.content,) #装换成markdown
        return article_lists
    
    def get_context_data(self, **kwargs):
        
        # 增加额外的数据，这里返回一个文章分类，以字典的形式
        kwargs['category_list'] = Category.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)
    

# class ArticleDetailView(DetailView):
#     #指定视图获取的model
#     model = Article
#     #指定渲染的模板文件
#     template_name = 'article_details.html'
#     #在html文件中使用的上下文名字
#     context_object_name='article_content'
#     
#     #为了让其以markdown形式：
#     def get_object(self):
#         obj = super(ArticleDetailView,self).get_object()
#         obj.body = markdown2.markdown(object.body)
#         return obj
    
    
        
