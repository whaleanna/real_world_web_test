#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 13:54
# @Author  : 邹金利
from base.base_util import BaseUtil
from common.string_method import StringMethod
from common.yaml_util import YamlUtil
from page_object.login_page import LoginPage
import allure, pytest

from page_object.register_page import RegisterPage

user = [[1, "leslie111@163.com", "leslie1234"], [2, " ", "leslie1234"], [3, "leslie111@163.com", " "]]

@allure.feature("登录模块")
class TestLogin(BaseUtil):

    @allure.story("登录已存在用户")
    def test_login(self):
        """
        登录已存在的用户
        :return:
        """
        lp = LoginPage(self.driver)
        lp.login_action()
        assert lp.get_except_result() == True, "登录失败"
        lp.save_image()

    @allure.story("登录无效用户")
    def test_login_invalid_user(self):
        """
        登录无效用户
        :return:
        """
        email = StringMethod.random_email(8)
        password = StringMethod.random_str(8)
        lp = LoginPage(self.driver)
        lp.login_action(email, password)
        assert lp.get_error_text() == "email or password is invalid", \
            "断言错误，预期:email or password is invalid, 实际:%s" % lp.get_error_text()

    # @allure.story("注册新账号登录")
    # def test_login(self):
    #     """
    #     注册新账号登录
    #     :return:
    #     """
    #     lp = LoginPage(self.driver)
    #     lp.register_action()
    #     assert lp.get_except_result() == True, "注册新号登录成功"

    @pytest.mark.parametrize("case_info", YamlUtil.read_get_data_yaml("/test_case/login_data.yml"))
    @allure.story("登录异常")
    def test_login_error(self, case_info):
        """
        登录异常
        :return:
        """
        email = case_info["data"]["email"]
        password = case_info["data"]["password"]

        lp = LoginPage(self.driver)
        lp.login_action(email, password)
        assert lp.get_error_text() == case_info["validate"], \
            "断言错误，预期:%s, 实际:%s" % (case_info["validate"], lp.get_error_text())

