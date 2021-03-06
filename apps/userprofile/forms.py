# -*- coding: utf-8 -*-
# @Time    : 2019-05-24 9:01
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : forms.py
# @Software: PyCharm

from django import forms
from django.contrib.auth.models import User
# from .models import Profile
from userprofile.models import UserProfile

class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField()
    password2 = forms.CharField()

    class Meta:
        model = UserProfile
        fields = ['username','email','phone','avatar','bio']

    def clean_password2(self):
        data = self.cleaned_data
        if data.get('password') == data.get('password2'):
            return data.get('password')
        else:
            raise forms.ValidationError("密码输入不一致,请重试")

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('email' , 'phone', 'avatar', 'bio')
