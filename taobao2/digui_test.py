# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

list3 = ['金色 4+32 全网通','黑色 4+32 全网通','玫瑰金 4+32 全网通','金色 4+64 全网通','黑色 4+64 全网通','玫瑰金 4+64 全网通','红色限量版 4+64']
list4 = ['官方标配']
list5 = ['64GB']
list6 = ['中国大陆']

s_list=[list3,list4,list5,list6]

# list1 = ['S','M','L','XL','XXL']
# list2 = ['黑色','海沫蓝','贝壳粉','白色','灰色','中国红']
#
# s_list=[list1, list2]
s=""

def commodity_pvs(s,n):

    if n == -1:
        return s # 递归特性一：必须有一个明确的结束条件
    else:
        str_list=[] # 每次创建一个空列表
        if isinstance(s,list): # s首次传进来是个空字符串，首次之后s将变成列表
            for i in s_list[n]: # 如果s是列表就遍历大列表中的第n个列表
                for j in s :  # 同时遍历上次循环返回的列表s
                    s_sum=i+j # 这一步很关键，把当前循环结果i加上上次列表里的循环结果，重新组成一对新值追加到列表
                    str_list.append(s_sum)
                    # print(str_list)
        else:
            for i in s_list[n]: # 把列表里的第n个列表遍历一遍取出值追加到空列表
                s_sum = i
                str_list.append(s_sum)
        s=str_list # 把当前列表当作参数传入下一次循环
        n=n-1 # 大列表下标减一
        print str_list[0]
        return commodity_pvs(s,n)  # 递归特性二：每次递归都是为了让问题规模变小


s=commodity_pvs(s, 3)  # 递归特性三：递归层次过多会导致栈溢出，且效率不高

for i in s:
    print i
