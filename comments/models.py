from django.db import models
from django.contrib.auth.models import User
from django.utils.six import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='commments'
    )
    email = models.EmailField(verbose_name='电子邮件')
    body = models.TextField()
    url = models.URLField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        'blog.Post',
        on_delete=models.CASCADE,
        related_name='comments'
    )

    def __str__(self):
        return self.body[:20]

    class Meta:
        ordering = ('-created_time',)
