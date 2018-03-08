# coding=utf-8
# 通过html抓取商品尺码和颜色
import re
import requests
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class PVS(object):

    def __commodity_pvs(self, s, n, big_list):

        if n == -1:
            return s  # 递归特性一：必须有一个明确的结束条件
        else:
            str_list = []  # 每次创建一个空列表
            if isinstance(s, list):  # s首次传进来是个空字符串，首次之后s将变成列表
                for i in big_list[n]:  # 如果s是列表就遍历大列表中的第n个列表
                    for j in s:  # 同时遍历上次循环返回的列表s
                        s_sum = i + '|' + j  # 这一步很关键，把当前循环结果i加上上次列表里的循环结果，重新组成一对新值追加到列表
                        str_list.append(s_sum)
                        # print(str_list)
            else:
                for i in big_list[n]:  # 把列表里的第n个列表遍历一遍取出值追加到空列表
                    s_sum = i
                    str_list.append(s_sum)
            s = str_list  # 把当前列表当作参数传入下一次循环
            n = n - 1  # 大列表下标减一
            # print str_list[0]
            return self.__commodity_pvs(s, n, big_list)  # 递归特性二：每次递归都是为了让问题规模变小

    def pvs(self, count, big_list, dict):
        # print '----------------------------------',count
        # print '++++++++++++++++++++++++++++++++++',big_list
        list = []
        s = ''
        # 商品属性列表
        Product_attributes_list = self.__commodity_pvs(s, count-1, big_list)  # 递归特性三：递归层次过多会导致栈溢出，且效率不高

        for i in Product_attributes_list:
            # print i
            single_commodity_list = i.split('|')
            pvs_string = ''
            for j in single_commodity_list:
                str = dict[j] + ';'
                for x in range(len(str)):
                    pvs_string += str[x]
            # print pvs_string
            list.append(pvs_string)
        return Product_attributes_list, list