# coding=utf-8
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# with open('1.txt') as f:
#     lines=f.readlines()
# with open('1.txt','w') as w:
#     for l in lines:
#         if(l.startswith('评论2')):
#             w.write(l.replace(b'\n',b'6666666666\n'))
#         else:
#             w.write(l)
#
# category_name = '女装'
# dir_name = '女装连衣裙1'
# id = '558924194248'
# path = "taobao_multimedia_datas/%s/%s/%s/评论/" % (category_name, dir_name, id)

# with open(path + '评论内容.txt') as f:
#     lines = f.readlines()
# with open(path + '评论内容.txt', 'w') as w:
#     for l in lines:
#         print l
#         str1 = '评论%s' % str(2 + 1)
#         append_content = '\t--->追加评论内容: *666666666888888***'
#         print str1, append_content
#         if (l.startswith('评论3')):
#             print 88888888888
#             w.write(l.replace(b'\n', b'6666666666\n'))
#         else:
#             w.write(l)

# num = 0
# num_length = 5
# while num < num_length:
#     append_str_info = 'fhthgfh'
#     if append_str_info:
#         print '---------------------'
#         print '评论%s' % str(num + 1),''.join(append_str_info)
#         print path
#         with open(path + '评论内容.txt') as f:
#             lines = f.readlines()
#         # ---------------------------------------------------------------------------
#         with open(path + '评论内容.txt', 'w') as w:
#             for l in lines:
#                 # print l
#                 str1 = '评论%s ' % str(num + 1)
#                 append_content = '\t--->追加评论内容:%s' % ''.join(append_str_info)
#                 # print str1, append_content
#                 if (l.startswith(str1)):
#                     print '********************************************'
#                     print str1
#                     w.write(l.replace(b'\n', append_content + '\n'))
#                     # break
#                 else:
#                     w.write(l)
#                     # img_big_list.append(img_list)
#     num += 1

print time.strftime('%Y_%m_%d_%T').replace(':', '_')