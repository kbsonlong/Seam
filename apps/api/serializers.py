# -*- coding: utf-8 -*-
# @Time    : 2019-06-22 21:46
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : serializers.py
# @Software: PyCharm
from rest_framework import serializers
from blog.models import Post


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','body','author','category','tags')
