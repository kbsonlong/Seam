# -*- coding: utf-8 -*-
# @Time    : 2019-05-24 21:21
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meat:
        model =Comment
        fields = ['body','email','url']