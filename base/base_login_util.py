#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 23:15
# @Author  : 邹金利
#
# from selenium import webdriver
# from common.yaml_util import YamlUtil
# from page_object.login_page import LoginPage
#
#
# class BaseLoginUtil:
#     """
#     包含登录的基础类
#     """
#     url = YamlUtil.read_get_data_yaml("/config.yml")["url"]
#
#     def setup(self):
#         print("基础")
#         # 设置全局driver，避免执行完之后自动关闭浏览器
#         global driver
#         self.driver = webdriver.Chrome()
#         driver = self.driver
#
#         # 窗口最大化
#         self.driver.maximize_window()
#         self.driver.implicitly_wait(10)
#         # 加载网页
#         self.driver.get(self.url)
#         lp = LoginPage(self.driver)
#         lp.login_action()
