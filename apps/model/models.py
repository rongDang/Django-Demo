from django.db import models
from mdeditor.fields import MDTextField


class Shop(models.Model):
    # 设置id为主键，自增，在字段中加上verbose_name那个在后台添加那个信息时，字段名会变为你写的名字
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15, verbose_name='标题')
    price = models.IntegerField(verbose_name='价格')
    # 这个是markdown的字段，保存我们的写的博客内容
    content = MDTextField()

    class Meta:
        # admin后台可以看到名称变为中文博客了
        verbose_name = "博客"
        # verbose_name_plural意思为博客名的复数名，如果不添加的话，后台显示: 博客s
        verbose_name_plural = verbose_name

    # 解决显示不明确的项目标题
    def __str__(self):
        return self.name


class Scoce(models.Model):
    C = models.IntegerField(default=0)
    python = models.IntegerField(default=0)
    Django = models.IntegerField(default=0)
    # on_delete=models.CASCADE 是联级删除，主表(Student)删除了，从表(Scoce)链接的数据也会被删除
    Student = models.ForeignKey('Student', on_delete=models.CASCADE)

    class Meta:
        # admin后台可以看到名称变为中文博客了
        verbose_name = "成绩"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.C)


class Student(models.Model):
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=3)
    tel = models.CharField(max_length=11)

    class Meta:
        # admin后台可以看到名称变为中文博客了
        verbose_name = "学生"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

