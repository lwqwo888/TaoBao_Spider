# coding=utf-8
import os
import re
import sys
import time
from collections import Counter

reload(sys)
sys.setdefaultencoding('utf-8')

with open('taobaourl.txt', 'rb') as f:
    lines = f.readlines()
    print lines
    # for line in lines:
