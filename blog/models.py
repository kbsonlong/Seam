from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


# Create your models here.

#分类模型
class Category(models.Model):
    name = models.CharField(max_length=50,verbose_name="分类")

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

##标签模型
class Tags(models.Model):
    name = models.CharField(max_length=50,verbose_name="标签")
    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


##文章模型
class Post(models.Model):
    title = models.CharField(max_length=150,verbose_name="标题")
    body = models.TextField(verbose_name="正文",null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="作者")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,verbose_name="分类")
    tag = models.ManyToManyField(Tags,null=True,blank=True,verbose_name="标签")
    create_time = models.DateTimeField(verbose_name="发布时间",auto_created=True,blank=True,null=True)
    modified_time = models.DateTimeField(verbose_name="更新时间",auto_now=True)
    total_views = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "博文"
        verbose_name_plural = verbose_name
        ordering = ('-create_time',)

    def __str__(self):
        return self.title

    def increase_views(self):
        self.total_views += 1
        self.save(update_fields=['total_views'])

        # 获取文章地址
    def get_absolute_url(self):
        return reverse('blog:post', args=[self.pk])
