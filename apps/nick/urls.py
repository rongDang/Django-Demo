# -*- encoding:utf8 -*-
from django.contrib import admin
from django.urls import path, include
from nick import views
app_name = "nick"

urlpatterns = [
    path('index/', views.index, name="main"),
    path('show/<msg>', views.show, name="show_data"),
    path('blog_index/', views.blog_index),
]
