---
title: README
tags:
  - Django
  - 自动化运维
categories:
  - Django
  - 自动化运维
date: 2019-06-22 20:27
status: publish
comment_status: open
Blog: https://www.alongparty.cn
Email: kbsonlong@gmail.com
Author: kbsonlong
---

###   django_rest_framework 使用简要说明

#### 1. 安装django、djangorestframework
```text
pip install django
pip install djangorestframework
```

#### 2. 创建项目
```text
django-admin startproject Seam .  # Note the trailing '.' character
cd tutorial
django-admin startapp blog
cd ..

```

#### 3. 添加模型models
```python
from django.db import models
from django.contrib.auth.models import User

##文章模型
class Post(models.Model):
    title = models.CharField(max_length=150,verbose_name="标题")
    body = models.TextField(verbose_name="正文",null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="作者")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,verbose_name="分类")
    tag = models.ManyToManyField(Tags,null=True,blank=True,verbose_name="标签")
    create_time = models.DateTimeField(verbose_name="发布时间",auto_now=True)
    modified_time = models.DateTimeField(verbose_name="更新时间",auto_now=True)

    class Meta:
        verbose_name = "博文"
        verbose_name_plural = verbose_name
        ordering = ('-create_time',)

    def __str__(self):
        return self.title
```

#### 4. 创建序列化Serializers
```python
from rest_framework import serializers
from blog.models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','body','author','category','tag')

```

#### 5. 创建Api视图
```python
from rest_framework import viewsets

from blog.models import Post
from api.serializers import PostSerializers

class PostApiView(viewsets.ModelViewSet):
    """
    API endpoint that allows Post to be viewed or edited.
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializers

```

#### 6. 配置url,(Seam/urls.py)
```python
from django.urls import include, path
from rest_framework import routers
from api.views import blog


router = routers.DefaultRouter()
router.register(r'posts', blog.PostApiView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

#### 7. 配置settings
```python
INSTALLED_APPS = (
    ...
    'rest_framework',
)

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10
}


```

#### 8. 同步数据库
```text
python manage.py makemigrations

python manage.py migrate

python manage.py createsuperuser --email admin@example.com --username admin

```

#### 9. 启动服务
```text
python manage.py runserver
```

![Api](media/screens/api.png)
![Postapi](media/screens/postapi.png)
