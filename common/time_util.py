#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/25 08:46
# @Author  : 邹金利
import time
import datetime
from functools import wraps


def timestamp():
    """时间戳"""
    return time.time()


def dt_strftime(fmt="%Y%m"):
    """
    datetime格式化时间
    :param fmt "%Y%m%d %H%M%S
    """
    return datetime.datetime.now().strftime(fmt)


def sleep(seconds=1.0):
    """
    睡眠时间
    """
    time.sleep(seconds)


def running_time(func):
    """函数运行时间"""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = timestamp()
        res = func(*args, **kwargs)
        print("Done！用时%.3f秒！" % (timestamp() - start))
        return res

    return wrapper