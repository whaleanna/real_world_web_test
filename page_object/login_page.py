#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 14:01
# @Author  : 邹金利

from selenium.webdriver.common.by import By
from page_object.register_page import RegisterPage


class LoginPage(RegisterPage):
    # 页面元素定位
    switch_login_loc = (By.LINK_TEXT, "Sign in")
    sign_in_loc = (By.XPATH, "//button[@type='submit']")

    # 页面操作
    def login_action(self, email="leslie111@163.com", password="leslie111"):
        self.click(self.switch_login_loc, case_name="切换到登录页面")
        self.set_keys(self.email_loc, email, case_name="输入邮箱")
        self.set_keys(self.password_loc, password, case_name="输入密码")
        self.click(self.sign_in_loc, case_name="点击登录按钮")



