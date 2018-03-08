# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

with open('1.txt') as f:
    lines=f.readlines()
with open('1.txt','w') as w:
    for l in lines:
        if(l.startswith('评论2')):
            w.write(l.replace(b'\n',b'6666666666\n'))
        else:
            w.write(l)

category_name = '女装'
dir_name = '女装连衣裙1'
id = '562735022799'
path = "taobao_multimedia_datas/%s/%s/%s/评论/" % (category_name, dir_name, id)

with open(path + '评论内容.txt') as f:
    lines = f.readlines()
with open(path + '评论内容.txt', 'w') as w:
    for l in lines:
        print l
        str1 = '评论%s' % str(2 + 1)
        append_content = '\t--->追加评论内容: *666666666888888***'
        print str1, append_content
        if (l.startswith('评论3')):
            print 88888888888
            w.write(l.replace(b'\n', b'6666666666\n'))
        else:
            w.write(l)