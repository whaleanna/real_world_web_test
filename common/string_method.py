#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 17:56
# @Author  : 邹金利
import math
import random
import string


class StringMethod:
    """
    构造异常测试数据,调用get_all_exception_test_data()
    获取到数据列表,之后同个PYtest框架里的parametrize()方
    法进行循环
    """

    @classmethod
    def random_str(cls, random_length=16):
        """
        生成一个指定长度的随机字符串，其中
        string.digits=0123456789
        string.ascii_letters=abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
        """
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(random_length)]
        random_str = ''.join(str_list)
        return random_str

    @classmethod
    def random_int(cls, random_length=8):
        """
        生成一个指定长度的随机数字
        """
        random_int = random.randint(math.pow(10, (random_length - 1)), math.pow(10, random_length) - 1)
        return random_int

    @classmethod
    def random_email(cls, random_length=None, email_type=None):
        email_type_list = ["@qq.com", "@163.com", "@126.com"]
        # 如果没有指定邮箱类型，默认在 email_type_list中随机一个
        if email_type == None:
            random_email_str = random.choice(email_type_list)
        else:
            random_email_str = email_type
        # 如果没有指定邮箱长度，默认在4-10之间随机
        if random_length == None:
            leng = random.randint(4, 10)
        else:
            leng = int(random_length)
        number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
        random_prefix = "".join(random.choice(number) for i in range(leng))
        email = random_prefix + random_email_str
        return email

