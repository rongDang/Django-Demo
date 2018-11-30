from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from nick.models import *
import markdown
from pure_pagination import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required


def index(request):
    # from django.core.mail import send_mail
    # 因为在settings中已经配置了邮箱设置，第三个是发件者，后面的是收件者,发送时页面会一直加载
    # send_mail("测试邮件", "First Django email QQ", "2801293031@qq.com", ["2801293031@qq.com"], fail_silently=False)
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
    }
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    names = ["小明", "小白", "小黑", "小花", "小二"]

    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(names, 2, request=request)
    people = p.page(page)

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


# Django分页器效果的展示
def page(request):
    names = Blog.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(names, 2, request=request)
    people = p.page(page)
    return render(request, 'nick/page.html', locals())


# 测试评论功能
def comment(request):
    # 因为评论需要绑定一个对象，所以随便给了一篇博客作为评论的对象
    blog = Blog.objects.get(id=1)
    return render(request, 'nick/comment.html', locals())


def blog_index(request):
    blog = Blog.objects.all().order_by("-create_time")
    # 分页测试
    try:
        # 获取当前页面，默认为1
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    paginator = Paginator(blog, 2, request=request)
    data = paginator.page(page)
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
