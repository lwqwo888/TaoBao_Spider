# coding=utf-8
import time
import datetime
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.loadImages"] = False

driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.implicitly_wait(5)
driver.get("https://qiang.taobao.com/category.htm?categoryId=312000")
js = "window.scrollTo(0, document.body.scrollHeight)"
# j = 1
# while j < 8:
#     driver.execute_script(js)
#     driver.implicitly_wait(0.1)
#     driver.save_screenshot("淘抢购%s.png" % j)
#     pageSource = driver.page_source
#     # print pageSource
#     j += 1

driver.execute_script(js)
driver.save_screenshot("淘抢购.png")
driver.execute_script(js)
driver.save_screenshot("淘抢购.png")
driver.execute_script(js)
driver.save_screenshot("淘抢购.png")
driver.execute_script(js)
driver.save_screenshot("淘抢购.png")
driver.execute_script(js)
driver.execute_script(js)
driver.save_screenshot("淘抢购.png")
driver.execute_script(js)
driver.save_screenshot("淘抢购.png")
driver.execute_script(js)
driver.save_screenshot("淘抢购.png")
pageSource = driver.page_source
html = etree.HTML(pageSource)
xpath_str = '''/html/body/div[@class="module"]//div[@class="content"]/div[@class="category-box"]/div[@class="qg-category-list"]/a/@href'''
urls = html.xpath(xpath_str)
j = 0
for i in urls:
    j += 1
    print i
print j