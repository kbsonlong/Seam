# -*- coding: utf-8 -*-
# @Time    : 2019-05-24 21:21
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : forms.py
# @Software: PyCharm

from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Comment


class CommentForm(forms.ModelForm):
    text =  forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Comment
        # fields = [ 'email', 'url', 'text']
        fields = [ 'text']