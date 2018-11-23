from django.contrib import admin
from nick.models import *
# Register your models here.


@admin.register(Boy)
class Boy_Admin(admin.ModelAdmin):
    list_display = ('id', 'username')


@admin.register(Girl)
class Girl_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')



@admin.register(Category)
class Category_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Tag)
class Tag_Admin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Blog)
class Blog_Admin(admin.ModelAdmin):
    list_display = ('id', 'title',  'click_nums', 'category', 'create_time')
    fields = ('title', 'content', 'category', 'tag')    # 编辑页面中要显示的字段
    # exclude = ('number') 在编辑页面排除该字段
    filter_horizontal = ('tag', )   # 对页面中多对多字段排版设置
    # 可以这样设置几个字段在一行例如：fields=(('title','tag'), 'content')这样title和tag是一行了

    # 重写模型保存的方法，保存博客时将该博客的分类数与标签数分别添加到对应的表中
    def save_model(self, request, obj, form, change):
        # obj是当前保存的博客内容，
        obj.save()
        # 博客分类数据的统计更新
        obj_category = obj.category  # 获取博客类别对象
        category_number = obj_category.blog_set.count()     # 反向查询
        obj_category.number = category_number
        obj_category.save()
        # 博客标签的统计更新，因为博客和标签是多对多关系，所以先获取所有的标签，后逆向查讯每个标签下对应的博客数量
        # 关于标签更新问题: obj.tag.all()不能获取到当前文章的标签，所以不能根据当前文章更新标签中的数目，
        # 也就只能在下次保存文章时再更新上次的标签数量，所以在视图函数中再写一遍更新
        obj_tag_list = Tag.objects.all()
        for obj_tag in obj_tag_list:
            tag_number = obj_tag.blog_set.count()
            obj_tag.number = tag_number
            obj_tag.save()

    # 对应的博客删除时，修改对应的分类数和标签数
    def delete_model(self, request, obj):
        obj.delete()
        # 博客分类数据的统计更新
        obj_category = obj.category
        category_number = obj_category.blog_set.count()
        obj_category.number = category_number
        obj_category.save()

        # 博客标签的统计更新，
        obj_tag_list = Tag.objects.all()
        for obj_tag in obj_tag_list:
            tag_number = obj_tag.blog_set.count()
            obj_tag.number = tag_number
            obj_tag.save()

