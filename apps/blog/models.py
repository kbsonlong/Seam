from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import markdown
from django.utils.html import strip_tags
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
    author = models.ForeignKey('userprofile.UserProfile',on_delete=models.SET_NULL,null=True,blank=True,verbose_name="作者")
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,verbose_name="文章分类")
    # 文章标签
    tags = models.ManyToManyField(Tags, blank=True,verbose_name="文章标签")
    create_time = models.DateTimeField(verbose_name="发布时间",auto_now_add=True,blank=True,null=True)
    modified_time = models.DateTimeField(verbose_name="更新时间",auto_now=True)
    total_views = models.PositiveIntegerField(default=0)
    # 文章标题图
    avatar = models.ImageField(upload_to='article/%Y%m%d/', blank=True)
    excerpt = models.CharField(max_length=200, blank=True)

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
        return reverse('blog:detail', args=[self.pk])

    # 保存时处理图片
    def save(self, *args, **kwargs):
        # 如果没有填写摘要
        if not self.excerpt:
            # 首先实例化一个 Markdown 类，用于渲染 body 的文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
            ])
            # 先将 Markdown 文本渲染成 HTML 文本
            # strip_tags 去掉 HTML 文本的全部 HTML 标签
            # 从文本摘取前 54 个字符赋给 excerpt
            self.excerpt = strip_tags(md.convert(self.body))[:54]

        # 调用原有的 save() 的功能
        article = super(Post, self).save(*args, **kwargs)

        # 固定宽度缩放图片大小
        if self.avatar and not kwargs.get('update_fields'):
            image = Image.open(self.avatar)
            (x, y) = image.size
            new_x = 400
            new_y = int(new_x * (y / x))
            resized_image = image.resize((new_x, new_y), Image.ANTIALIAS)
            resized_image.save(self.avatar.path)
        return article
