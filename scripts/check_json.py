# -*- coding: utf-8 -*-

"""

author: nicolas-kings
date: 2024-04-24
description: 核对json结构

"""

import json


# 读取外部JSON文件
def load_external_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


# 检查缺少的字段
def check_missing_fields(json_data, fields_to_check):
    missing_fields = []
    for index, item in enumerate(json_data):
        for field in fields_to_check:
            if field not in item:
                missing_fields.append((index, field))
    return missing_fields


# 外部JSON文件路径  idiom.json
json_file_path = "../archived/idiom-dirty.json"

# 加载外部JSON数据
json_data = load_external_json(json_file_path)

# 自定义要检查的字段列表
custom_fields_to_check = ['word', 'derivation', 'example', 'explanation', 'pinyin', 'abbreviation']


# 检查缺少的字段
missing_fields = check_missing_fields(json_data, custom_fields_to_check)

# 输出缺少字段的对象索引和字段名
if missing_fields:
    print("缺少的字段：")
    for index, field in missing_fields:
        print(f"对象 {index} 缺少字段 '{field}'")
else:
    print("所有对象都包含了所需的字段。")
