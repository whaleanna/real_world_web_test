#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 13:45
# @Author  : 邹金利

from selenium import webdriver


class BaseUtil:
    @classmethod
    def setup_class(cls):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        cls.driver = webdriver.Chrome(options=chrome_options)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
