# -*- coding:utf-8 -*-
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtCore import QEventLoop
import lxml.html
from bs4 import BeautifulSoup

url = 'https://zhuanlan.zhihu.com/p/27363298'

app = QApplication([])
webview = QWebView()
loop = QEventLoop()

webview.loadFinished.connect(loop.quit)
webview.load(QUrl(url))
loop.exec_()
html = webview.page().mainFrame().toHtml()
#tree = lxml.html.fromstring(html)
#fixed_html = lxml.html.tostring(tree, pretty_print=True)
soup = BeautifulSoup(html, 'html.parser')
fixed_html = soup.prettify()
title = soup.find(class_="PostIndex-title av-paddingSide av-titleFont")
#print(fixed_html)
print(title)