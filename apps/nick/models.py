from django.db import models
from django.utils import timezone
from mdeditor.fields import MDTextField
from django.contrib.auth.models import User
import uuid


def image_upload_to(instance, filename):
    return 'img/{}'.format(uuid.uuid4().hex+filename)


# 创建多对多测试表
class Boy(models.Model):
    username = models.CharField(max_length=10)
    # 测试头像
    head = models.ImageField(upload_to=image_upload_to, default='http://img3.duitang.com/uploads/item/201505/22/20150522205616_KeX3C.jpeg')

    def __str__(self):
        return self.username


class Girl(models.Model):
    name = models.CharField(max_length=10)
    # 多对多关系的键，该键在Girl表中，类似外键，
    b = models.ManyToManyField("Boy")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(verbose_name="博客类别", max_length=20)
    # number为该类别下存在多少博客
    number = models.IntegerField(default=2)

    class Meta:
        verbose_name = "类别"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(verbose_name="博客标签", max_length=20)
    # number为对应标签下存在的博客,这里设置默认值是因为该字段是后续添加的
    number = models.IntegerField(default=1)

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=50, verbose_name='标题')
    content = MDTextField(verbose_name='博客内容')
    create_time = models.DateTimeField(verbose_name='创建时间', default=timezone.now)
    click_nums = models.IntegerField(verbose_name='点击量', default=0)
    # 类别和博客是一对多的关系
    category = models.ForeignKey(Category, verbose_name='文章类别', on_delete=models.CASCADE)
    # 博客和标签是多对多的关系v
    tag = models.ManyToManyField(Tag, verbose_name='文章标签')

    class Meta:
        verbose_name = "博客"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


"""
    评论回复模型的设计，Comments是用户对博客的评论表，而CommentReply是对评论的回复，
    这里设计的是二级评论，CommentReply是对评论进行的评论表，也就是二级评论，它往上找的一级评论只能是comments中的
    这里就有个问题，如果commentReply评论了commentReply的内容的话  找不到它的父级评论?只能找到它的comments的内容。。。
    
    Django使用两个app创建外键时对‘auth.User’产生了多对多的依赖所以报错。
    解决方法就算在创建model字段时，使用related_name如下面表所示
"""


class Comments(models.Model):
    # entry对应评论的对象，这里的对象是博客
    entry = models.ForeignKey(Blog, related_name="entry", on_delete=models.CASCADE)
    content = MDTextField()
    author = models.ForeignKey(User, related_name="author", on_delete=models.CASCADE)
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s 评论了 %s' % (self.author.username, self.entry)


class CommentReply(models.Model):
    # comment是对评论的回复，对应的
    comment = models.ForeignKey(Comments, related_name='comment_reply', null=True, on_delete=models.CASCADE)
    content = MDTextField()
    author_form = models.ForeignKey(User, related_name='author_form', null=True, on_delete=models.CASCADE)
    author_to = models.ForeignKey(User, related_name='author_fo', null=True, on_delete=models.CASCADE)
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s @ %s' % (self.author_form.username, self.author_to.username)


# 多级评论的表设计，如下所示,如果它没有父级评论则就是对文章的评论，如果有父级评论则是对评论的回复
class Discuss(models.Model):
    blog = models.ForeignKey('Blog', related_name='blog', on_delete=models.CASCADE)
    content = MDTextField()
    # parent_discuss 是当前评论的父级评论，它可以为空，为空的话当前评论就是对文章的评论而不是对评论的回复
    parent_discuss = models.ForeignKey('Discuss', blank=True, null=True, related_name='p_discuss', on_delete=models.CASCADE)
    name = models.ForeignKey(User, related_name='name', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s 评论了 %s' % (self.name.username, self.parent_discuss)










