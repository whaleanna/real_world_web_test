#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 14:02
# @Author  : 邹金利

from selenium.webdriver.common.by import By
from base.base_object import BasePage
from common.string_method import StringMethod


class RegisterPage(BasePage):

    # 页面元素定位
    switch_register_loc = (By.LINK_TEXT, "Sign up")
    username_loc = (By.XPATH, "//input[@placeholder='Username']")
    email_loc = (By.XPATH, "//input[@type='email']")
    password_loc = (By.XPATH, "//input[@type='password']")
    sign_up_loc = (By.XPATH, "//button[@type='submit']")
    error_text_loc = (By.XPATH, "//li[@ng-repeat='error in errors']")
    your_feed_loc = (By.LINK_TEXT, "Your Feed")

    user_default = StringMethod.random_str(6)
    email_default = StringMethod.random_email(6)

    # 页面操作
    def register_action(self, username=user_default, email=email_default, password=user_default):
        self.click(self.switch_register_loc, case_name="切换到注册页面")
        self.set_keys(self.username_loc, username, case_name="输入用户名")
        self.set_keys(self.email_loc, email, case_name="输入邮箱")
        self.set_keys(self.password_loc, password, case_name="输入密码")
        self.click(self.sign_up_loc, case_name="点击注册按钮")

    def get_except_result(self):
        return self.locator_element(self.your_feed_loc).is_enabled()

    def get_error_text(self):
        return self.locator_element(self.error_text_loc).text
