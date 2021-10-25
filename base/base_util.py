#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 13:45
# @Author  : 邹金利

from selenium import webdriver
from common.yaml_util import YamlUtil
import os

class BaseUtil:

    url = YamlUtil.read_get_data_yaml("/config.yml")["url"]

    def setup(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

        # 设置全局driver，避免执行完之后自动关闭浏览器
        # global driver
        # self.driver = webdriver.Chrome()
        # driver = self.driver

        # 窗口最大化
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        # 加载网页
        self.driver.get(self.url)

    def teardown(self):
        self.driver.quit()
