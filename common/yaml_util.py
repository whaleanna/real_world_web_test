#!usr/bin/python
# -*- coding: UTF-8 -*-
# @Time    : 2021/10/24 17:58
# @Author  : 邹金利

import yaml, os

root_path = os.path.dirname(os.path.dirname(__file__))


class YamlUtil:
    @classmethod
    def read_get_data_yaml(cls, yaml_name):
        with open(root_path + yaml_name, "r", encoding="utf-8") as file:
            value = yaml.load(stream=file, Loader=yaml.Loader)
            return value

    @classmethod
    def write_extract_yaml(cls, data, yaml_name):
        with open(root_path + yaml_name, "a", encoding="utf-8") as file:
            value = yaml.dump(data=data, stream=file)
            return value

    @classmethod
    def clean_extract_yaml(cls, yaml_name):
        with open(root_path + yaml_name, "w", encoding="utf-8") as file:
            file.truncate()
