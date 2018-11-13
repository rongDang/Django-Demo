from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.db import connection
from model.models import *
from django.db.models import Count, Avg, Sum
import json

def index(request):
    # 从链接中获得参数，参数为model则跳转到model的首页中去
    if request.GET.get("name") == "nick":
        return redirect(reverse("nick:main"))
    return render(request, 'model/index.html')


def year(request, year):
    return HttpResponse("测试使用2.1版本:"+str(year))


# 作业1
def work(request):
    return render(request, 'model/work1.html')


def show_work(request):
    if request.method == "POST":
        # 采用原生SQL语言删除
        id = request.POST["id"]
        cur = connection.cursor()
        cur.execute("delete from student where id='%s'" % id)
        connection.commit()
        return HttpResponse("1")
    name = request.GET.get("name")
    score = request.GET.get("score")
    return render(request, 'model/show.html', locals())


# 作业2
def work2(request):
    id = request.GET.get("id")
    # 添加成绩操作
    if request.method == "POST":
        print(id)
        stu_id = request.POST["id"]
        C = request.POST["c"]
        python = request.POST["python"]
        django = request.POST["django"]
        name = Student.objects.get(id=stu_id)
        # 这里需要注意的是，外键是int类型，所以赋值绑定也需要是int类型
        role = Scoce(C=int(C), python=int(python), Django=int(django), Student_id=name.id).save()
        return HttpResponse("1")
    if id:
        role = Student.objects.get(id=id)
        score = role.scoce_set.all()
    return render(request, 'model/work2.html', locals())


# 作业2
def work3(request):
    id = request.GET.get("id")
    if id:
        score = list(Scoce.objects.filter(Student_id=id).values('id', 'C', 'Django', 'python'))
        return HttpResponse(json.dumps(score))
    student = Student.objects.filter()
    return render(request, 'model/work3.html', locals())


# Django模型的操作
def CRUD(request):
    # 查看模型执行的MySQL语句, query方法
    sql = Student.objects.all().query
    # values 获取字典形式的结果,values_list获取元组结果
    stu_info = Student.objects.all()
    # aggregate函数来对数据进行运算操作,查找所有数据id的条数,
    number = Student.objects.all().aggregate(Count('id'))
    # Student和Scoce联查, 通过获取主表数据对象，通过 主表对象.***_set 来获取和主表关联的所有从表数据
    student = Student.objects.get(id=2)
    score = student.scoce_set.all()
    # filter中的参数使用,具体看笔记
    one = Student.objects.filter(name__contains='小红').filter()
    two = Student.objects.filter(name__icontains='小').all()
    return render(request, 'model/CRUD.html', locals())
