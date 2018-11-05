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
    path('delete/', views.delete, name='delete'),
]

