# -*- encoding:utf8 -*-
# Django上下文渲染器，可以理解为全局函数
from django.db import connection


def ip_address(request):
    return {'ip': request.META['REMOTE_ADDR']}


def work_data(request):
    cur = connection.cursor()
    cur.execute("select * from student")
    result = cur.fetchall()
    return {"data": result}

