from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from nick.models import *
import markdown


def index(request):
    # 从链接中获得参数，参数为model则跳转到model的首页中去,reverse反转网址，
    if request.GET.get("name") == "model":
        # reverse("model:main",arg={}),后面的arg={}是可以给网址的参数
        return redirect(reverse("model:main"))
    return render(request, "nick/one.html")


def show(request, msg):
    title = "using django templates"
    student = {
        "s1": {"name": "小白", "age": 20, "sex": "man", "scroe": 90},
        "s2": {"name": "小黑", "age": 20, "sex": "man", "scroe": 99},
        "s3": {"name": "小红", "age": 99, "sex": "woman", "scroe": 100},
        "s4": {"name": "小碘", "age": 20, "sex": "man", "scroe": 89},
    }
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    names = ["小明", "小白", "小黑", "小花", "小二"]
    # 下面为多对多关系的查询，
    boy = Boy.objects.all()
    for i in boy:
        # i.girl_set.count()，逆向查询女孩的数量
        print(i.username, i.girl_set.count())
    girl = Girl.objects.all()
    for i in girl:
        # 正向查询男孩的数量
        print(i.name, i.b.all())
    return render(request, "nick/show.html", locals())


def blog_index(request):
    blog = Blog.objects.filter().values('id', 'title', 'create_time')
    return render(request, 'nick/index.html', locals())


def blog_content(request, title):
    data = Blog.objects.get(title=title)
    # 正向查询该博客关联的类别，标签
    categoty = data.category.name
    tags = data.tag.all()
    # 使用markdown解析数据库中的博客内容
    content = markdown.markdown(data.content, extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])
    return render(request, 'nick/content.html', locals())


def blog_class(request, title):
    categories = Category.objects.all()
    return render(request, 'nick/classify.html', locals())


def blog_class_details(request, title):
    data = Category.objects.get(name=title)
    # 反向查询从表blog中的数据
    result = data.blog_set.all()
    return render(request, 'nick/classify_details.html', locals())


def tags(request, title):
    tags = Tag.objects.all()
    obj_tag_list = Tag.objects.all()
    for obj_tag in obj_tag_list:
        tag_number = obj_tag.blog_set.count()
        obj_tag.number = tag_number
        obj_tag.save()
    return render(request, 'nick/tags.html', locals())


def tag(request, title):
    data = Tag.objects.get(name=title)
    result = data.blog_set.all()
    return render(request, 'nick/tag.html', locals())
