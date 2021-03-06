# -*- encoding:utf8 -*-
from django.urls import path
from nick import views
app_name = "nick"

urlpatterns = [
    path('index/', views.index, name="main"),
    path('show/<msg>', views.show, name="show_data"),
    path('page/', views.page),
    path('comment/', views.comment, name='comment'),
    path('comments/', views.comments, name='comments'),
    path('test_comments', views.test_comments, name='test_comments'),
    path('test_submit', views.test_submit, name='submit'),
    path('upload/', views.upload, name='up_img'),
    # 个人博客测试页面
    path('blog_index/', views.blog_index, name="blog_index"),
    path('blog_content/<title>', views.blog_content, name="blog_content"),
    path('blog_class/<title>', views.blog_class, name="blog_class"),
    path('blog_class_details/<title>', views.blog_class_details, name="blog_class_details"),
    path('blog_tags/<title>', views.tags, name='blog_tags'),
    path('blog_tag/<title>', views.tag, name='blog_tag'),
]
