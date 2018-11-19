from django.contrib import admin
from nick.models import *
from mdeditor.widgets import MDEditorWidget
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
    list_display = ('id', 'title', 'content',  'click_nums', 'category', 'create_time')
