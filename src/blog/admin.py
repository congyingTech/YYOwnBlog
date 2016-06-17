from django.contrib import admin

from blog.models import Article, Category


# Register your models here.
#do not forget register here.
admin.site.register(Article)
admin.site.register(Category)