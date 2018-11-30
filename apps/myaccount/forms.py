# -*- encoding:utf8 -*-
from django import forms
from .models import UserProfile
"""
    创建了两个表单，一个是更新用户资料时使用，一个是重写用户登录表单
    重写用户登录表单，是因为django-allauth在用户注册时只会创建User对象，不会创建与之关联的UserProfile对象
    我们希望用户在注册时两个对象一起被创建，并存储到数据库中去
"""


class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
    org = forms.CharField(label='Organization', max_length=50, required=False)
    telephone = forms.CharField(label='Telephone', max_length=50, required=False)


class SignupForm(forms.Form):
    """
    因为django-allauth在用户注册只会创建User对象，不会创建与之关联的UserProfile对象，
    我们希望用户在注册时两个对象一起被创建，并存储到数据库中。
    """
    def signup(self, request, user):
        print("使用自定义的注册表单")
        user_profile = UserProfile()
        user_profile.user = user
        user.save()
        user_profile.save()

