#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 20:07
# @Author  : 邹金利

from base.base_util import BaseUtil
from common.yaml_util import YamlUtil
import allure,pytest

from page_object.register_page import RegisterPage


@allure.feature("注册模块")
class TestRegister(BaseUtil):

    @pytest.fixture(scope='function', autouse=True)
    def open_web(self):
        """打开网页"""
        lp = RegisterPage(self.driver)
        lp.get_url()

    @pytest.mark.parametrize("case_info", YamlUtil.read_get_data_yaml("/test_case/register_data.yml"))
    @allure.story("注册异常")
    def test_register_error(self, case_info):
        """
        登录异常
        :return:
        """
        username = case_info["data"]["username"]
        email = case_info["data"]["email"]
        password = case_info["data"]["password"]

        lp = RegisterPage(self.driver)
        lp.register_action(username, email, password)
        assert lp.get_error_text() == case_info["validate"], \
            "断言错误，预期:%s, 实际:%s" % (case_info["validate"], lp.get_error_text())

    @allure.story("成功注册")
    @pytest.mark.smoke
    def test_register(self):
        """
        注册新用户
        :return:
        """
        lp = RegisterPage(self.driver)
        lp.register_action()
        assert lp.get_except_result() == True, "登录失败"

    # @allure.story("重复注册")
    # def test_register(self):
    #     """
    #     重复注册
    #     :return:
    #     """
    #     lp = RegisterPage(self.driver)
    #     lp.register_action()
