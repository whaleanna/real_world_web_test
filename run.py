#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 14:33
# @Author  : 邹金利
import shutil
import pytest, os


if __name__ == "__main__":
    try:
        shutil.rmtree('report/result_json')
    except Exception:
        pass
    pytest.main()
    os.system('allure generate ./report/result_json -o ./report/allure-report --clean')
