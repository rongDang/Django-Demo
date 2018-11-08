from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.db import connection
from model.models import *
from django.db.models import Count, Avg, Sum

def index(request):
    # 从链接中获得参数，参数为model则跳转到model的首页中去
    if request.GET.get("name") == "nick":
        return redirect(reverse("nick:main"))
    return render(request, 'model/index.html')


def year(request, year):
    return HttpResponse("测试使用2.1版本:"+str(year))


def work(request):
    return render(request, 'model/work1.html')


def show_work(request):
    name = request.GET.get("name")
    score = request.GET.get("score")
    return render(request, 'model/show.html', locals())


def delete(request):
    id = request.POST["id"]
    cur = connection.cursor()
    cur.execute("delete from student where id='%s'" % id)
    connection.commit()
    return HttpResponse("1")


# Django模型的操作
def CRUD(request):
    # 查看模型执行的MySQL语句
    sql = Student.objects.all().query
    # values 获取字典形式的结果,values_list获取元组结果
    stu_info = Student.objects.values('id', 'name', 'sex', 'tel')
    # aggregate函数来对数据进行运算操作,查找所有数据id的条数
    number = Scoce.objects.all().aggregate(Count('id'))
    # Student和Scoce联查
    name = Student.objects.values('name')
    scoces = name.values('python')
    print(name, scoces)
    return render(request, 'model/CRUD.html', locals())
