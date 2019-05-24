# -*- coding: utf-8 -*-
# @Time    : 2019-05-23 17:24
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : forms.py
# @Software: PyCharm

from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body','category']

    def __init__(self,*args,**kwargs):
        super(PostForm,self).__init__(*args,**kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            if field_name in ["m_ipmi_user", "m_ipmi_passwd"]:
                field.widget.attrs.update({'class': 'form-control'})
            else:
                field.widget.attrs.update({'class': 'form-control'})
