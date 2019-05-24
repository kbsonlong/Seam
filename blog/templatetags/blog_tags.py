# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 17:03
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : blog_tags.py
# @Software: PyCharm

from django import template
from ..models import Post,Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all()[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()