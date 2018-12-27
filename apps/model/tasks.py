# -*- encoding:utf8 -*-
from celery.task import task
import time


@task
def test_celery():
    print("开始")
    time.sleep(6)
    return "test celery"



