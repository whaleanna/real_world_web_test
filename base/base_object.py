#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 13:45
# @Author  : 邹金利
import allure,os
from selenium import webdriver
from common.allure_step_util import AllureMethod


class BasePage(AllureMethod):

    def __init__(self, driver):
        self.driver = driver

    def locator_element(self, locator):
        """
        元素定位
        :param locator:
        :return:
        """
        return self.driver.find_element(*locator)

    def set_keys(self, locator, value, case_name=None):
        """
        设置元素关键字
        :param locator:
        :return:
        """
        self.save_data(case_name+": " + str(value))
        return self.locator_element(locator).send_keys(value)

    def click(self, locator, case_name=None):
        """
        元素点击
        :param locator:
        :return:
        """
        self.save_data(case_name)
        self.locator_element(locator).click()

    def goto_frame(self, frame_name, case_name=None):
        """
        切换frame
        :return:
        """
        self.save_data(case_name)
        self.driver.switch_to.frame(frame_name)

    def switch_frame(self, frame_name, case_name=None):
        """
        切换frame
        :return:
        """
        self.save_data(case_name)
        self.driver.switch_to.frame(frame_name)

    def exit_frame(self, case_name=None):
        """
        退出frame
        :return:
        """
        self.save_data(case_name)
        self.driver.switch_to.default_content()

    def execute_script(self, target, case_name=None):
        """
        执行JS脚本
        :return:
        """
        self.save_data(case_name)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    # def get_error_text(self, loc):
    #     return self.locator_element(self.error_text_loc).text

    def save_screenshot(self):
        """
        截图
        :return:
        """
        root_path = os.path.dirname(os.path.dirname(__file__))
        image_path = os.path.join(root_path, "image")
        image_path = os.path.join(image_path, "success.png")
        try:
            picture_url = self.driver.save_screenshot(image_path)
            print("%s ：截图成功！！！" % picture_url)
        except BaseException as msg:
            print("%s ：截图失败！！！" % msg)
        return image_path

    def save_image(self):
        """
        保存图片到allure报告：后续可以遇到失败截图
        :return:
        """
        file_path = self.save_screenshot()
        with open(file_path, 'rb') as f:
            file = f.read()
            allure.attach(file, "截图", allure.attachment_type.PNG)


