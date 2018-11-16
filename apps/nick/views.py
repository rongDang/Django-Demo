from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
# Create your views here.


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
    return render(request, "nick/show.html", locals())


def blog_index(request):
    return render(request, 'nick/index.html')
