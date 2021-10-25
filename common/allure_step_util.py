#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 17:56
# @Author  : 邹金利
import allure


class AllureMethod:

    @classmethod
    def save_data(cls, name=None):
        if name is not None:
            with allure.step(name):
                pass
