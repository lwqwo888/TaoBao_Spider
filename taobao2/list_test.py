# coding=utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# list1 = ['S','M','L','XL','XXL']
# list2 = ['黑色','海沫蓝','贝壳粉','白色','灰色','中国红']
# list1_len = len(list1)
# list2_len = len(list2)
# y = 0
# while y < list1_len:
#     z = 0
#     while z < list2_len:
#         print (list1[y] + list2[z])
#         z += 1
#     y += 1
#
# # print [m + n for m in list1 for n in list2 ]
#
# print('\n')
#
# list3 = ['金色 4+32 全网通','黑色 4+32 全网通','玫瑰金 4+32 全网通','金色 4+64 全网通','黑色 4+64 全网通','玫瑰金 4+64 全网通','红色限量版 4+64']
# list4 = ['官方标配']
# list5 = ['64GB']
# list6 = ['中国大陆']
# list7 = [m + n + a + b for m in list3 for n in list4 for a in list5 for b in list6]
# for i in list7:
#     print (i)
#









class A(object):

    def __b(self):
        string = ''
        str = u"追加字符"
        for i in range(len(str)):
            string += str[i]
        print string

    def c(self):
        self.__b()

if __name__ == '__main__':
    # A().__b()
    A().c()





