"""Demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # 要用这个markdown的富文本编辑器需要引入它的路径
    path('mdeditor/', include('mdeditor.urls')),
    # 可以理解为flask中的蓝图,model模块中有很多的视图函数对应在model中的urls中，
    # 要使用model中的那些url需要在Django项目的url中进行绑定注册才能使用。
    path('model/', include('model.urls')),
    # 直接写对应app的名字导入路径文件，nick.urls(建议使用)
    path('nick/', include('nick.urls'))
]

if settings.DEBUG:
    # 配置上传静态文件的路径
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print(urlpatterns)
