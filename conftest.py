#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import base64
import pytest
import allure
from py.xml import html
from selenium import webdriver

from config.conf import cm
from common.time_util import timestamp

driver = None


@pytest.fixture(scope='session', autouse=True)
def drivers(request):
    global driver
    if driver is None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        # driver = webdriver.Chrome()
        # driver.maximize_window()

    # def final_quit():
    #     driver.quit()

    # request.addfinalizer(final_quit)
    return driver

#@pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item):
#     """
#     当测试失败的时候，自动截图，展示到html报告中
#     :param item:
#     """
#     pytest_html = item.config.pluginmanager.getplugin('html')
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
#     extra = getattr(report, 'extra', [])
#
#     if report.when == 'call' or report.when == "setup":
#         xfail = hasattr(report, 'wasxfail')
#         if (report.skipped and xfail) or (report.failed and not xfail):
#             screen_img = _capture_screenshot()
#             if screen_img:
#                 html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:1024px;height:768px;" ' \
#                        'onclick="window.open(this.src)" align="right"/></div>' % screen_img
#                 extra.append(pytest_html.extras.html(html))
#         report.extra = extra
#
# def _capture_screenshot():
#     """截图保存为base64"""
#     now_time, screen_file = cm.screen_path
#     driver.save_screenshot(screen_file)
#     allure.attach.file(screen_file, "失败截图{}".format(now_time), allure.attachment_type.PNG)
#     with open(screen_file, 'rb') as f:
#         imagebase64 = base64.b64encode(f.read())
#     return imagebase64.decode()

