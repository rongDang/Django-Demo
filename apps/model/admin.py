from django.contrib import admin
from model.models import *
# 注册模型，显示在admin界面中，便于管理


# 注册student模型管理器
@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    # 设置要显示在界面中的字段
    list_display = ('id', 'name', 'sex', 'tel')
    # 添加可以修改的字段
    # list_editable = ('name', 'sex', 'tel')
    # 每页显示的条数
    list_per_page = 10
    # 根据id排序
    ordering = ('id',)


# 注册User模型
@admin.register(Scoce)
class Scoce_Admin(admin.ModelAdmin):
    list_display = ('id', 'C', 'python', 'Django', 'Student')
    ordering = ('id',)


# 注册shop模型
@admin.register(Shop)
class Shop_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'content')
