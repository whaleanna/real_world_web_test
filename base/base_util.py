#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 13:45
# @Author  : 邹金利

from selenium import webdriver

class BaseUtil:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
