# -*- encoding:utf8 -*-
from django.urls import path
from myaccount import views
app_name = "myaccount"

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile_update'),
]

