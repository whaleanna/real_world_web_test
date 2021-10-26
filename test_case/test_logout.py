#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 13:53
# @Author  : 邹金利
from base.base_util import BaseUtil
from selenium import webdriver

from page_object.logout_page import LogoutPage
import allure,pytest


@allure.feature("注销登录模块")
class TestLogout(BaseUtil):

    @pytest.fixture(scope='function', autouse=True)
    def open_web(self):
        """打开网页"""
        lp = LogoutPage(self.driver)
        lp.get_url()

    @allure.story("注销登录")
    @pytest.mark.smoke
    def test_logout(self, drivers):
        """
        注销登录(登录已存在的用户->注销)
        :return:
        """
        lgp = LogoutPage(self.driver)
        lgp.logout_action()
        assert lgp.get_except_result() == True, "退出登录失败"
