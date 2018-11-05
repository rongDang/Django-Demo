# -*- encoding:utf8 -*-
# Django上下文渲染器，可以理解为全局函数


def ip_address(request):
    return {'ip': request.META['REMOTE_ADDR']}


def work_data(request):
    return {"data": {"小白": "95", "小花": "82", "小六": "96", "小黑": "80"}}

