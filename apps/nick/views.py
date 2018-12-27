from django.shortcuts import render, redirect, reverse
from pure_pagination import Paginator, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from nick.models import *
import markdown, os
from .forms import MDEditorForm


def index(request):
    # from django.core.mail import send_mail
    # 因为在settings中已经配置了邮箱设置，第三个是发件者，后面的是收件者,发送时页面会一直加载
    # send_mail("小苗同学", "这是一个测试邮件", "2801293031@qq.com", ["1954404140@qq.com"], fail_silently=False)
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


# 测试评论功能，使用djano-comments，只有评论，没有回复功能
def comment(request):
    # 因为评论需要绑定一个对象，所以随便给了一篇博客作为评论的对象
    blog = Blog.objects.get(id=1)
    return render(request, 'nick/comment.html', locals())


# 测试评论功能，带有回复的功能,二级评论，没有完成，有问题
def comments(request):
    blog = Blog.objects.get(id=1)  # Django博客模型
    # 查询该博客下有多少评论
    comments = Comments.objects.filter(entry=blog.id)
    replys = []
    for i in comments:
        replys.append(CommentReply.objects.filter(comment=i.id))
        print(CommentReply.objects.filter(comment=i.id))
        # replay = CommentReply.objects.get(comment=i.id)
    # 二级评论需要有和谁关联的一级评论，通过这个一级评论来找到它下面的二级评论，二级评论有个问题
    # reply = CommentReply.objects.filter(comment=comments[0].id)
    form = MDEditorForm()
    return render(request, 'nick/commtents.html', locals())


# 多级评论, 评论的渲染有点问题
def test_comments(request):
    blog = Blog.objects.get(id=1)
    comments = Discuss.objects.filter(blog=blog.id)
    form = MDEditorForm()
    one = []
    for comm in comments:
        b={}
        b["id"] = comm.id
        b["content"] = markdown.markdown(comm.content, extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        one.append(b)
    return render(request, 'nick/test_comments.html', locals())


# 评论表单数据的提交
def test_submit(request):
    # reply是被回复的评论，
    user_id = request.user.id
    reply = request.POST.get("reply")
    blog = request.POST.get("blog")
    content = request.POST.get("content")
    print(reply, blog, content)
    Discuss.objects.create(content=content, blog_id=blog, name_id=user_id, parent_discuss_id=reply)
    return HttpResponse("1")


def allowed_file(filename):
    IMG = ["png", "jpg", "gif", "jpeg"]  # 允许的拓展名
    # 判断文件格式,使用rsplit()从右向左寻找,参数1是只分割一次，lower()将字符串大写转换为小写
    # print(filename.rsplit(".", 1))
    return "." in filename and filename.rsplit(".", 1)[1].lower() in IMG


# post上传头像
def upload(request):
    if request.method == 'POST':
        from Demo1.settings import MEDIA_ROOT
        boy = Boy.objects.get(username='小白')
        img = request.FILES.get('img')
        if allowed_file(str(img)):
            try:
                os.remove(MEDIA_ROOT+"/"+str(boy.head))
            except:
                pass
            boy.head = img
            boy.save()
            src = Boy.objects.get(username='小白').head
            return HttpResponse(str(src))
        else:
            return HttpResponse('error')
    return render(request, 'nick/test.html')


def blog_index(request):
    # print(request.user.id)
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
    # 更新标签数目
    obj_tag_list = Tag.objects.all()
    for obj_tag in obj_tag_list:
        # 正向
        tag_number = obj_tag.blog_set.count()
        obj_tag.number = tag_number
        obj_tag.save()
    return render(request, 'nick/tags.html', locals())


def tag(request, title):
    data = Tag.objects.get(name=title)
    result = data.blog_set.all()
    return render(request, 'nick/tag.html', locals())
