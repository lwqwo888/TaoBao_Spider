# coding=utf-8
import re

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


list1 = []
zidian = {}
zidian1 = {}
test = [u'XXL\u4e2d\u56fd\u7ea2']
list = [u'\u9ed1\u8272', u'\u6d77\u6cab\u84dd', u'\u8d1d\u58f3\u7c89', u'\u767d\u8272', u'\u7070\u8272', u'\u4e2d\u56fd\u7ea2']
dict = {'S': u'\u9ed1\u8272 \u6d77\u6cab\u84dd \u8d1d\u58f3\u7c89 \u767d\u8272 \u7070\u8272 \u4e2d\u56fd\u7ea2', 'M': u'\u9ed1\u8272 \u6d77\u6cab\u84dd \u8d1d\u58f3\u7c89 \u767d\u8272 \u7070\u8272 \u4e2d\u56fd\u7ea2', 'L': u'\u9ed1\u8272 \u6d77\u6cab\u84dd \u8d1d\u58f3\u7c89 \u767d\u8272 \u7070\u8272 \u4e2d\u56fd\u7ea2', 'XL': u'\u9ed1\u8272 \u6d77\u6cab\u84dd \u8d1d\u58f3\u7c89 \u767d\u8272 \u7070\u8272 \u4e2d\u56fd\u7ea2', 'XXL': u'\u9ed1\u8272 \u6d77\u6cab\u84dd \u8d1d\u58f3\u7c89 \u767d\u8272 \u7070\u8272 \u4e2d\u56fd\u7ea2'}
print list
print dict

if dict['S'] == '黑色 海沫蓝 贝壳粉 白色 灰色 中国红':
    print 6666
print '\u9ed1\u8272 \u6d77\u6cab\u84dd \u8d1d\u58f3\u7c89 \u767d\u8272 \u7070\u8272 \u4e2d\u56fd\u7ea2'.decode('unicode-escape')
s = u'\u9ed1\u8272 \u6d77\u6cab\u84dd \u8d1d\u58f3\u7c89 \u767d\u8272 \u7070\u8272 \u4e2d\u56fd\u7ea2'.decode('utf-8')
list1.append(s)

print list1

a = ' '.join(list)
zidian['l'] = a.decode('utf-8')
print zidian

zidian1['w'] = '你好'
print zidian1
{'X': u'L\u9ed1\u8272 XL\u9ed1\u8272 L\u6d77\u6cab\u84dd XL\u6d77\u6cab\u84dd L\u8d1d\u58f3\u7c89 XL\u8d1d\u58f3\u7c89 L\u767d\u8272 XL\u767d\u8272 L\u7070\u8272 XL\u7070\u8272 L\u4e2d\u56fd\u7ea2 XL\u4e2d\u56fd\u7ea2', 'S': u'\u9ed1\u8272 \u6d77\u6cab\u84dd \u8d1d\u58f3\u7c89 \u767d\u8272 \u7070\u8272 \u4e2d\u56fd\u7ea2', 'M': u'\u9ed1\u8272 \u6d77\u6cab\u84dd \u8d1d\u58f3\u7c89 \u767d\u8272 \u7070\u8272 \u4e2d\u56fd\u7ea2', 'L': u'\u9ed1\u8272 \u6d77\u6cab\u84dd \u8d1d\u58f3\u7c89 \u767d\u8272 \u7070\u8272 \u4e2d\u56fd\u7ea2'}


