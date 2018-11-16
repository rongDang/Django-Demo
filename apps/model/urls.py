# -*- encoding:utf8 -*-
from django.contrib import admin
from django.urls import path, include
from model import views
app_name = "model"

urlpatterns = [
    # 这里设置接收的参数设置为整型，使用<>从url中捕获值
    path('year/<int:year>', views.year),
    path('index/', views.index, name="main"),
    path('work/', views.work, name='work'),
    path('show_work/', views.show_work, name='show'),
    path('CURD/', views.CRUD),
    path('work2/', views.work2, name='work2'),
    path('work3/', views.work3, name='work3'),
    path('work4/', views.work4, name='work4'),
    path('one/<id>', views.show_bolg, name='blog'),
    path('editor/', views.show_editor, name='editor'),
]

