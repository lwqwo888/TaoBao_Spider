# !/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import jsonpath
import requests

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'
city_json = requests.get(url).text
print(city_json)

# json字符串转换为python字典对象
city_dict = json.loads(city_json)
# print(city_dict)

# 使用jsonpath匹配
# 获取根节点下的所有name节点的值
names = jsonpath.jsonpath(city_dict, expr='$..name')
print(names)
# 根节点下的message节点的值
message = jsonpath.jsonpath(city_dict, expr='$.message')
print(message)
# D节点下的前3个
D = jsonpath.jsonpath(city_dict, expr='$.content.data.allCitySearchLabels.D[3].code')
print(D)
# D节点下的第2个和第4个
D = jsonpath.jsonpath(city_dict, expr='$.content.data.allCitySearchLabels.D[1,3]')
print(D)