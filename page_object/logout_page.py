#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 14:01
# @Author  : 邹金利
import time

from selenium.webdriver.common.by import By
from base.base_object import BasePage
from page_object.login_page import LoginPage
import pytest

class LogoutPage(BasePage):

    # 页面元素定位
    switch_login_loc = (By.LINK_TEXT, "Sign in")
    settings_loc = (By.XPATH, "//a[@ui-sref='app.settings']")
    logout_loc = (By.XPATH, "//button[@ng-click='$ctrl.logout()']")

    # 页面操作
    def logout_action(self):
        lp = LoginPage(self.driver)
        lp.login_action()

        self.click(self.settings_loc, case_name="点击设置")
        time.sleep(2)
        target = self.locator_element(self.logout_loc)
        self.execute_script(target, case_name="滑动到注销登录按钮的位置")
        self.click(self.logout_loc, case_name="点击注销按钮")

    def get_except_result(self):
        return self.locator_element(self.switch_login_loc).is_enabled()
