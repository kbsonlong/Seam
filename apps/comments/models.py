from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible
##引入富文本插件
from ckeditor.fields import RichTextField
##引入评论树级插件
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.

@python_2_unicode_compatible
class Comment(MPTTModel):
    user = models.ForeignKey(
        'userprofile.UserProfile',
        on_delete=models.CASCADE,
        related_name='commments',
        default='',
        null=True,
        blank=True
    )
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = RichTextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)

    # 新增，mptt树形结构
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children'
    )

    # 新增，记录二级评论回复给谁, str
    reply_to = models.ForeignKey(
        'userprofile.UserProfile',
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='replyers'
    )

    def __str__(self):
        return self.text[:20]


    class MPTTMeta:
        order_insertion_by = ['-created_time']
