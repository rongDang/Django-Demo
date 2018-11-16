# -*- encoding:utf8 -*-
from django.template.library import Library

register = Library()


# 自定义的Django过滤器，要使用templatetags包，需要先到setting中注册当前的Django应用
@register.filter()
def square(a, b):
    # 这里传入的a为要过滤的对象，b为对过滤对象的操作
    return int(a) ** int(b)
