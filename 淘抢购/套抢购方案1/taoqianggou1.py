# coding=utf-8
import time
import datetime
from lxml import etree
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 导入 webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.loadImages"] = False
# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
driver = webdriver.PhantomJS(desired_capabilities=dcap)
driver.get("https://qiang.taobao.com/category.htm?categoryId=312000")
driver.implicitly_wait(2)
# 获取页面名为 wrapper的id标签的文本内容
# data = driver.find_elements_by_class_name("qg-category-list")
# js = "var q=document.documentElement.scrollTop=100000"
js = "window.scrollTo(0, document.body.scrollHeight)"
j = 1
while j < 8:
    driver.execute_script(js)

    # driver.implicitly_wait(0.1)
    driver.save_screenshot("淘抢购%s.png" % j)
    pageSource = driver.page_source
    # datas = driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div[2]")
    # data = driver.find_elements_by_class_name("qg-category-list")
    # for i in datas:
    #     print i.text
    j += 1
# driver.execute_script(js)
# driver.save_screenshot("淘抢购9.png")
# datas = driver.find_elements(By.XPATH, "/html/body/div[2]/div[2]/div/div[1]/div/div[2]")
# driver.implicitly_wait(5)
# print len(data)


html = etree.HTML(pageSource)
xpath_str = '''/html/body/div[@class="module"]//div[@class="content"]/div[@class="category-box"]/div[@class="qg-category-list"]/a/@href'''
urls = html.xpath()
n = 0
for i in urls:
    n += 1
    print i

