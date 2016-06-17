"""YYOwnBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from blog import views


urlpatterns = [
    #这里url是决定浏览器中输入什么
    url(r'^blog/$', views.IndexView.as_view(), name='article_list'),
    #url(r'^blog/details/(?P<article_id>\d+)$', views.ArticleDetailView.as_view(), name = 'article_details'),
    
    #url(r'^blog/', 'article.views.IndexView'),
    url(r'^admin/', admin.site.urls),
    #url(r'^test/$', 'article.views.test')
    #url(r'^$', blog.views.IndexView.as_view()), # this will get function from view 
]
