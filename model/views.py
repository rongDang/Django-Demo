from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.db import connection


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

