# -*- coding: utf-8 -*-
# @Time    : 2019-05-24 21:23
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views
app_name = 'comments'

urlpatterns = [
    path('post_comment/<int:post_pk>/',views.post_comment,name='post_comment'),
    path('post_comment/<int:post_pk>/<int:parent_comment_id>',views.post_comment,name='comment_reply'),
]