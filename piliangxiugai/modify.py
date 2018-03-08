# coding=utf-8
import os
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def url_process(url):
    res = re.compile(r'(\?|&)id=(\d+).*?', re.S)
    id = res.search(url).group(2)
    # print id
    return ''.join(id)

if __name__ == '__main__':
    path = os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir))
    print path
    with open('taobaourl.txt', 'rb') as f:
        lines = f.readlines()
    for line in lines:
        id = url_process(line)
        print id
        path_old = path + "/abc/" + id + '/'
        print path_old
        if (os.path.exists(path_old)):
            print 'old_path------:', path_old
            os.rename(path_old, path + "/abc/" + "666666")
        else:
            print "路径不存在"