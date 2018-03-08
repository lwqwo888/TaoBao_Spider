# coding=utf-8
import re
import requests
from lxml import etree
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

list3 = []
list1 = ['S','M','L','XL','XXL']
list2 = ['黑色','海沫蓝','贝壳粉','白色','灰色','中国红']
list4 = ['1','2','3']
# list1_len = len(list1)
# list2_len = len(list2)
# y = 0
# while y < list1_len:
#     z = 0
#     while z < list2_len:
#         print list1[y] + list2[z]
#         z += 1
#
#     y += 1
#
# # list3 = []
# list1 = ['a','b']
# list3.append(list1)
# list2 = ['1','2']
# list3.append(list2)
#
# for i in list3:
#     print i

# def x(num):
#     lis = []
#     for i in range(num):
#         lis.append([])
#     return lis
# cs = x(2)
# cs[0].append(1)
# print cs


# print [m + n + q for m in list1 for n in list2 for q in list4]
# print [m + n + q for m in 'ABCD' for n in 'XYZ' for q in '123']
# list3 = [list1, list2]
# num = len(list3)
# i = 0
# while i < num:
#
#     i += 1
# y = 0

# while y < size_length:
#     z = 0
#     while z < pvs_length:
#         key1 = data_property_list[y]
#         key2 = data_pvs_list[z]
#         print '**************',key1,key2
#         print data_property_dict[key1] + data_pvs_list[key2]
#         z += 1
#
#     y += 1
# for n in data_property_list:
#     print n


# def fact(n):
#     return fact_iter(n, 1)
#
# def fact_iter(num, product):
#     if num == 1:
#         return product
#     return fact_iter(num - 1, num * product)
#
# print fact(5)


def fact(n):
    if n==1:
        return 1
    print n
    return n * fact(n - 1)
print fact(5)