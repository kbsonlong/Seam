# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 13:41
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : urls.py
# @Software: PyCharm

from django.urls import path
from . import views

app_name = 'blog'
urlpatterns =[
    path('',views.IndexView.as_view(),name='index'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='detail'),
    path('post_delete/<int:pk>/',views.post_delete,name='post_delete'),
    path('post_create/',views.PostCreateView.as_view(),name='post_create'),
    path('post_update/',views.PostUpdateView.as_view(),name='post_update'),
]