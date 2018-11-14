from django.db import models
from mdeditor.fields import MDTextField


class Shop(models.Model):
    # 设置id为主键，自增
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    price = models.IntegerField()
    # 这个是markdown的字段，保存我们的写的博客内容
    content = MDTextField()

    # 解决显示不明确的项目标题
    def __str__(self):
        return self.name


class Scoce(models.Model):
    C = models.IntegerField(default=0)
    python = models.IntegerField(default=0)
    Django = models.IntegerField(default=0)
    # on_delete=models.CASCADE 是联级删除，主表(Student)删除了，从表(Scoce)链接的数据也会被删除
    Student = models.ForeignKey('Student', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.C)


class Student(models.Model):
    name = models.CharField(max_length=10)
    sex = models.CharField(max_length=3)
    tel = models.CharField(max_length=11)

    def __str__(self):
        return self.name

