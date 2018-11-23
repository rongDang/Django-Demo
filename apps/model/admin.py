from django.contrib import admin
from model.models import *
# 注册模型，显示在admin界面中，便于管理


class MyAdminSite(admin.AdminSite):
    site_header = "Django测试页面"  # 此处设置页面显示标题
    site_title = "test-title"       # 此处设置页面头部标题


# admin_site = MyAdminSite(name='management') 此处括号内name值必须设置，否则将无法使用admin设置权限，随便什么值
admin_site = MyAdminSite(name="management")

# 下面方法一样可以修改后台的登录标题和页面头部标题
# admin.site.site_header = '登录标题'
# admin.site.site_title = '头部title'


# 注册student模型管理器
@admin.register(Student)
class Student_Admin(admin.ModelAdmin):
    """
    用户登录时判断是什么用户，如果是普通用户则只能看到自己的数据？
    def get_queryset(self, request):
        st = super(Student_Admin, self).get_queryset(request)
        if request.user.is_superuser:
            return st
        return st.filter(user=Student.objects.filter(name=request.user))

    """
    # 设置要显示在界面中的字段
    list_display = ('id', 'name', 'sex', 'tel')
    # 设置哪些字段可以点击进入编辑界面
    list_display_links = ('id', 'name')
    # 添加可以修改的字段
    list_editable = ('sex', )
    # 每页显示的条数
    list_per_page = 10
    # 根据id排序
    ordering = ('id',)

    # 筛选器
    list_filter = ('name', 'sex')  # 过滤器
    search_fields = ('name', 'tel')  # 搜索字段


# 注册User模型
@admin.register(Scoce)
class Scoce_Admin(admin.ModelAdmin):
    list_display = ('id', 'C', 'python', 'Django', 'Student')
    ordering = ('id',)


# 注册shop模型
@admin.register(Shop)
class Shop_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'content')
