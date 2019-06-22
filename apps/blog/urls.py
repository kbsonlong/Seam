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
    path('post_update/<int:pk>/',views.PostUpdateView.as_view(),name='post_update'),
    # path('post_update/<int:id>/',views.article_update,name='post_update'),
    path('category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path('tag/<int:pk>/', views.TagView.as_view(), name='tag'),
    path('archives/<int:year>/<int:month>/', views.ArchivesView.as_view(), name='archives'),
]