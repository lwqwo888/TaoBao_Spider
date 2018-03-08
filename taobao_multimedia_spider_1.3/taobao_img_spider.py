# coding=utf-8
# version: 1.1
# 脚本功能: 淘宝商品图片获取
# 参数: id(id), category_name(分类文件夹名), dir_name(商品文件夹名),
# date : 2018-02-11
# Creator: lwq
import os
import re
import time
import gzip
import Queue
import random
import urllib
import urllib2
import requests
import StringIO
import threading
import linecache
from lxml import etree
# from ChangeIP import change_ip
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class Taobao_Img(object):

    def __init__(self):
        current_path = os.path.split(os.path.realpath(__file__))[0]
        self.__file_log = open('%s/log/img_log%s.txt' % (current_path, time.strftime('%Y_%m_%d')), 'a+')
        self.mutex = threading.Lock()
        self.url = 'https://detail.tmall.com/item.htm?&id='
        # self.proxy = {"http": ""}
        # self.headers = ""
        self.html_data = ""
        self.res_data = ""
        self.sec = 0
        self.old_sec = 0

    def change_ip(self):
        new_sec = time.time()
        self.sec = new_sec - self.old_sec
        if self.sec > 0.3:
            # # 要访问的目标页面
            # targetUrl = "http://httpbin.org/ip"

            # 代理服务器
            proxyHost = "n10.t.16yun.cn"
            proxyPort = "6442"

            # 代理隧道验证信息
            proxyUser = "16SBYYUY"
            proxyPass = "658666"

            proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
                "host": proxyHost,
                "port": proxyPort,
                "user": proxyUser,
                "pass": proxyPass,
            }

            proxies = {
                "http": proxyMeta,
                "https": proxyMeta,
            }

            # tunnel = random.randint(1, 10000)
            # headers = {"Proxy-Tunnel": str(tunnel)}
            # resp = requests.get(targetUrl, proxies=proxies, headers=headers)
            self.proxy = proxies
        else:
            self.proxy = self.proxy

    def change_ua(self):
        tunnel = random.randint(1, 1036)
        # print tunnel
        user_agent = linecache.getline('1000ua-pc.log', tunnel)
        user_agent = user_agent.strip().replace('\n', '').replace('\r', '')
        # print user_agent
        self.headers = {
            'authority': 'detail.tmall.com',
            'method': 'GET',
            'scheme': "https",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            'accept-encoding': "gzip, deflate, br",
            'accept-language': "zh-CN,zh;q=0.9",
            'cache-control': "max-age=0",
            'cookie': "cna=XTyQEoI1uE4CAXBfh3IMFSpJ; cq=ccp%3D1; t=4d814acaeff7745d2b1df5c531cb7227; _tb_token_=3eb56ee77e988; cookie2=17B3F5F8A0D9CB4142FFBB0733EC948B; pnm_cku822=098%23E1hvApvUvbpvjQCkvvvvvjiPPL5wljtVP25hgjivPmPy1jYRRsdvzjiRR2z91jQPvpvhvvvvvvhCvvOvUvvvphvEvpCWh8%2Flvvw0zj7OD40OwoAQD7zheutYvtxr1RoKHkx%2F1RBlYb8rwZBleExreE9aWXxr1noK5FtffwLyaB4AVAdyaNoxdX3z8ikxfwoOddyCvm9vvvvvphvvvvvv96Cvpv9hvvm2phCvhRvvvUnvphvppvvv96CvpCCvkphvC99vvOC0B4yCvv9vvUvQud1yMsyCvvpvvvvviQhvCvvv9UU%3D; isg=ArOzZnnX7QJos6HBeuocdKfGQrcdQCLrPU38GWVQTFIJZNMG7bjX-hH2aqJx",
            'upgrade-insecure-requests': "1",
            # 'user-agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
            'user-agent': user_agent,
        }

    def test_change(self):
        self.change_ua()
        print self.headers

    def page_data(self, id):
        url = self.url + id
        print "当前商品链接：%s" % url
        # try:
        self.change_ua()
        # self.change_ip()
        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                self.html_data = response.text
                # print self.headers
                # print self.proxy

        except Exception as e:
            print '数据请求失败...正在重试......', e
            self.log(str(e))
            with open('request.log', 'a') as f:
                f.write('%s [程序]请求失败%s - %s\n' % (url, id, time.ctime()))

            # # global NETWORK_STATUS
            NETWORK_STATUS = False  # 请求超时改变状态

            if NETWORK_STATUS == False:
                #     '请求超时'
                for i in range(1, 11):
                    time.sleep(1)
                    print '请求失败，第%s次重复请求' % i
                    if i == 5:
                        print "[INFO]: 程序睡眠中......"
                        time.sleep(10)
                    self.change_ua()
                    # self.change_ip()
                    try:
                        response = requests.get(url, headers=self.headers)
                        if response.status_code == 200:
                            self.html_data = response.text
                            with open('request.log', 'a') as f:
                                f.write('%s 重新请求成功%s - %s\n' % (url, id, time.ctime()))
                            print ('[INFO]:重发请求成功!!!!!!!!!!')
                            break
                    except:
                        with open('request.log', 'a') as f:
                            f.write('%s 重新请求失败, 继续重试...%s - %s\n' % (url, id, time.ctime()))
                        print ('[INFO]:重发请求失败!!!!!!!!!!')
                        print '第%s次重复请求失败! 继续重试...' % i
                        continue
                if response.status_code == 200:
                    with open('request.log', 'a') as f:
                        f.write('%s 最终请求成功!!!!!%s - %s\n' % (url, id, time.ctime()))
                    print ('[INFO]:重发请求成功!!!!!!!!!!')
                else:
                    with open('request.log', 'a') as f:
                        f.write('%s 最终请求失败! ! ! ! !%s - %s\n' % (url, id, time.ctime()))
                    print ('[INFO]:重发请求失败!!!!!!!!!!')
        time.sleep(1)
        print self.headers
        self.res_data = etree.HTML(self.html_data)
        print "请求成功！"
        return self.res_data
        # except Exception as e:
        #     print e
        #     self.log(str(e))

    # 轮播图下载
    def turn_img(self, id, category_name, dir_name):
        # res = etree.HTML(self.html_data)
        ron = self.res_data.xpath('''//*[@id="J_UlThumb"]//a/img/@src|//*[@id="J_UlThumb"]//a/img/@data-src''')
        cover_img_list = []
        for err_url in ron:
            index_num = self.find_last(err_url, "_")
            cover_img_list.append(err_url[:index_num])
        for true_url in cover_img_list:
            # print '************', true_url
            with open("img_url.txt", 'a') as f:
                f.write("http:" + true_url + '\n')
                # print "http:" + true_url
        cover_img_list_length = len(cover_img_list)
        self.download_img(cover_img_list_length, cover_img_list, id, "carousel", category_name, dir_name)

    # 颜色图下载
    def color_img(self, id, category_name, dir_name):
        xpath_str1 = '''//*//div[@class="tb-skin"]//dl/dd/ul/li/a[@style]/span/text()'''
        xpath_str2 = '''//*//div[@class="tb-skin"]//dl/dd/ul/li/a/@style'''
        color_list = self.res_data.xpath(xpath_str1)
        err_color_url_list = self.res_data.xpath(xpath_str2)

        # 处理图片链接,只保留链接部分,删除其它字符
        color_url_list = []
        for err_color_url in err_color_url_list:
            index_num = self.find_last(err_color_url, "_")
            color_url = err_color_url[:index_num]
            color_url_list.append(color_url.split("(")[1])
        length = len(color_url_list)

        self.download_img(length, color_url_list, id, "color", category_name, dir_name, color_list)

    # 细节图下载
    def detail_img(self, id, category_name, dir_name):
        desc_url_obj = re.compile(r'''descUrl.*?('//(.*?)'|"//(.*?)")''', re.S)
        print self.html_data
        desc_url_list = desc_url_obj.findall(self.html_data)
        print desc_url_list
        desc_url = 'http:' + desc_url_list[0][0].replace('"', '').replace("'", '')
        # print desc_url
        # print '++++++++++++++++', self.proxy
        res = ""
        self.change_ua()
        self.change_ip()
        # res = requests.get(desc_url, headers=self.headers, proxies=self.proxy).content
        try:
            response = requests.get(desc_url, headers=self.headers, proxies=self.proxy)
            if response.status_code == 200:
                res = response.content
                # print self.headers
                # print self.proxy

        except Exception as e:
            print '数据请求失败...正在重试......', e
            self.log(str(e))
            with open('request.log', 'a') as f:
                f.write('%s [代理]请求失败%s - %s\n' % (desc_url, id, time.ctime()))
            # # global NETWORK_STATUS
            NETWORK_STATUS = False  # 请求超时改变状态

            if NETWORK_STATUS == False:
                #     '请求超时'
                for i in range(1, 11):
                    time.sleep(0.3)
                    print '请求失败，第%s次重复请求' % i
                    if i == 5:
                        print "[INFO]: 代理睡眠中......"
                        time.sleep(10)
                    self.change_ua()
                    self.change_ip()
                    try:
                        response = requests.get(desc_url, headers=self.headers, proxies=self.proxy)
                        if response.status_code == 200:
                            res = response.content
                            with open('request.log', 'a') as f:
                                f.write('%s 重新请求成功%s - %s\n' % (desc_url, id, time.ctime()))
                            print ('[INFO]:重发请求成功!!!!!!!!!!')
                            break
                    except:
                        with open('request.log', 'a') as f:
                            f.write('%s 重新请求失败, 继续重试...%s - %s\n' % (desc_url, id, time.ctime()))
                        print ('[INFO]:重发请求失败!!!!!!!!!!')
                        print '第%s次重复请求失败! 继续重试...' % i
                        continue

                if response.status_code == 200:
                    with open('request.log', 'a') as f:
                        f.write('%s 最终请求成功!!!!!%s - %s\n' % (desc_url, id, time.ctime()))
                    print ('[INFO]:重发请求成功!!!!!!!!!!')
                else:
                    with open('request.log', 'a') as f:
                        f.write('%s 最终请求失败! ! ! ! !%s - %s\n' % (desc_url, id, time.ctime()))
                    print ('[INFO]:重发请求失败!!!!!!!!!!')
        # print self.headers
        # print res
        img_url_obj = re.compile(r'(//img.*?\.(jpg|png|SS2|gif))', re.S)
        img_url_list = img_url_obj.findall(res)
        length = len(img_url_list)
        print "准备下载细节图"
        print '去重前url数量:', length
        temporary_img_url_list = []
        for i in img_url_list:
            temporary_img_url_list.append(i[0])
        news_img_url_list = list(set(temporary_img_url_list))
        news_img_url_list.sort(key=temporary_img_url_list.index)
        new_length = len(news_img_url_list)
        print '去重后url数量:', new_length
        for j in news_img_url_list:
            with open("img_url.txt", 'a') as f:
                f.write("http:" + j + '\n')
                # print "http:" + j
        self.download_img(new_length, news_img_url_list, id, "detail", category_name, dir_name)
        # with open('img_url.txt', 'rb') as f:
        #     lines = f.readlines()
            # print '///////////////////////',len(lines)

    # 下载器
    def download_img(self, list_length, list, id, name, category_name, dir_name, *args):
        data = ''
        k = 0
        while k < list_length:
            img_url = list[k]
            img_url = "http:" + img_url
            # 图片文件夹名
            doc_name = name + '_img'
            # taobao_multimedia_datas/女装/女装连衣裙1/id/img/name        /id+name
            path = "taobao_multimedia_datas/%s/%s/%s/img/%s/" % (category_name, dir_name, id, doc_name)
            # print name
            # print path
            if (not (os.path.exists(path))):
                os.makedirs(path)
            # 后缀名
            format = img_url[-4:]
            # print format
            if args:
                img_name = id + '_co' + str(k + 1)
            else:
                img_name = id + "_" + name + "_" + str(k+1)
            print "正在请求　%s" % name
            # try:
            self.change_ua()
            self.change_ip()
            try:
                response = requests.get(img_url, headers=self.headers, proxies=self.proxy)
                if response.status_code == 200:
                    data = response.content
                    # print self.headers
                    # print self.proxy

            except Exception as e:
                print '数据请求失败...正在重试......', e
                self.log(str(e))
                with open('request.log', 'a') as f:
                    f.write('%s [代理]请求失败%s - %s\n' % (img_url, id, time.ctime()))
                # # global NETWORK_STATUS
                NETWORK_STATUS = False  # 请求超时改变状态

                if NETWORK_STATUS == False:
                    #     '请求超时'
                    for i in range(1, 11):
                        time.sleep(0.3)
                        print '请求失败，第%s次重复请求' % i
                        if i == 5:
                            print "[INFO]: 代理睡眠中......"
                            time.sleep(10)
                        self.change_ua()
                        self.change_ip()
                        try:
                            response = requests.get(img_url, headers=self.headers, proxies=self.proxy)
                            if response.status_code == 200:
                                data = response.content
                                with open('request.log', 'a') as f:
                                    f.write('%s 重新请求成功%s - %s\n' % (img_url, id, time.ctime()))
                                print ('[INFO]:重发请求成功!!!!!!!!!!')
                                break
                        except:
                            with open('request.log', 'a') as f:
                                f.write('%s 重新请求失败, 继续重试...%s - %s\n' % (img_url, id, time.ctime()))
                            print ('[INFO]:重发请求失败!!!!!!!!!!')
                            print '第%s次重复请求失败! 继续重试...' % i
                            continue

                    if response.status_code == 200:
                        with open('request.log', 'a') as f:
                            f.write('%s 最终请求成功!!!!!%s - %s\n' % (img_url, id, time.ctime()))
                        print ('[INFO]:重发请求成功!!!!!!!!!!')
                    else:
                        with open('request.log', 'a') as f:
                            f.write('%s 最终请求失败! ! ! ! !%s - %s\n' % (img_url, id, time.ctime()))
                        print ('[INFO]:重发请求失败!!!!!!!!!!')

            print "正在保存　%s" % img_name
            with open(path + img_name + format, 'wb') as f:
                # print '******************',res
                f.write(data)
# --------------------------------------------------------------------------------------
            print '共%s个　第%s个url: %s' % (list_length, k+1, img_url)
            time.sleep(0)

            k += 1
        print "[INFO]: %s商品%s图片已抓取完成！！\n" % (id, name)

    # 找出指定字符在字符串中最后一次出现的下标
    def find_last(self, string, str):
        last_position = -1
        while True:
            # 在string字符串的last_position+1下标后面找不到str会返回-1
            position = string.find(str, last_position + 1)
            # print position
            if position == -1:
                return last_position
            last_position = position

    # 提取ID函数
    def url_process(self, url):
        res = re.compile(r'(\?|&)id=(\d+).*?', re.S)
        id = res.search(url).group(2)
        # print id
        return ''.join(id)

    def set_proxy(self):
        """
        设置代理
        """
        # 获取xicidaili的高匿代理
        proxy_info_list = []  # 抓取到的ip列表
        for page in range(1, 2):  # 暂时只抓第一页
            request = urllib2.Request('http://www.xicidaili.com/nn/%d' % page)
            request.add_header('Accept-Encoding', 'gzip, deflate')
            request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8')
            request.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en;q=0.6')
            request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36')
            response = urllib2.urlopen(request, timeout=5)

            headers = response.info()
            content_type = headers.get('Content-Type')
            if content_type:
                charset = re.findall(r"charset=([\w-]+);?", content_type)[0]
            else:
                charset = 'utf-8'
            if headers.get('Content-Encoding') == 'gzip':
                gz = gzip.GzipFile(fileobj=StringIO.StringIO(response.read()))
                content = gz.read().decode(charset)
                gz.close()
            else:
                content = response.read().decode(charset)
            response.close()
            print u'获取第 %d 页' % page
            ip_page = re.findall(r'<td>(\d.*?)</td>', content)
            proxy_info_list.extend(ip_page)
            time.sleep(random.choice(range(1, 3)))

        # 打印抓取的内容
        print u'代理IP地址\t端口\t存活时间\t验证时间'
        for i in range(0, len(proxy_info_list), 4):
            print u'%s\t%s\t%s\t%s' % (proxy_info_list[i], proxy_info_list[i + 1], proxy_info_list[i + 2], proxy_info_list[i + 3])

        all_proxy_list = []  # 待验证的代理列表
        # proxy_list = []  # 可用的代理列表
        for i in range(0, len(proxy_info_list), 4):
            proxy_host = proxy_info_list[i] + ':' + proxy_info_list[i + 1]
            all_proxy_list.append(proxy_host)

        # 开始验证

        # 单线程方式
        for i in range(len(all_proxy_list)):
            proxy_host = self.test(all_proxy_list[i])
            if proxy_host:
                break
        else:
            # TODO 进入下一页
            print u'没有可用的代理'
            return None

        # 多线程方式
        # threads = []
        # # for i in range(len(all_proxy_list)):
        # for i in range(5):
        #     thread = threading.Thread(target=test, args=[all_proxy_list[i]])
        #     threads.append(thread)
        #     time.sleep(random.uniform(0, 1))
        #     thread.start()
        #
        # # 等待所有线程结束
        # for t in threading.enumerate():
        #     if t is threading.currentThread():
        #         continue
        #     t.join()
        #
        # if not proxy_list:
        #     print u'没有可用的代理'
        #     # TODO 进入下一页
        #     sys.exit(0)
        print u'使用代理： %s' % proxy_host
        return proxy_host

    def test(self, proxy_host):
        """
        验证代理IP有效性的方法
        :param proxy_host:
        :return:
        """
        try:
            request = urllib2.Request('http://cn.bing.com/')  # 用于验证代理是否有效
            request.add_header(
                'User-Agent',
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36')
            urllib2.install_opener(urllib2.build_opener(urllib2.ProxyHandler({'http': proxy_host})))
            http_code = urllib2.urlopen(request, timeout=5).getcode()
            if http_code == 200:
                return proxy_host
        except Exception as e:
            print e
            return None

    def log(self, msg):
        self.mutex.acquire()
        self.__file_log.write(msg.encode('utf-8'))
        self.__file_log.write(u'\n'.encode('utf-8'))
        self.mutex.release()


if __name__ == '__main__':
    start = time.time()
    ti = Taobao_Img()
    ti.test_change()
    # with open('taobaourl.txt', 'rb') as f:
    #     lines = f.readlines()
    # category_name = '男鞋'
    # dir_name = '运动鞋'
    # id_list = []
    # for line in lines:
    #     id = ti.url_process(line)
    #     id_list.append(id)
    #     ti.page_data(id)
    #     ti.turn_img(id, category_name, dir_name)
    #     ti.color_img(id, category_name, dir_name)
    #     ti.detail_img(id, category_name, dir_name)
    #     print "[INFO]: %s商品所有图片抓取完成！！！！！！！！\n\n" % id
    # end = time.time()
    # time_s = end-start
    # print "[INFO]: 所有抓取任务已完成！共计用时%s秒\n\n" % time_s


    # url = "https://detail.tmall.com/item.htm?id=557200845972"
    # url = "https://item.taobao.com/item.htm?spm=a219r.lmn002.14.174.6f516358W81jq9&id=562441235623&ns=1&abbucket=16"
    # url = 'https://item.taobao.com/item.htm?spm=a219r.lm874.14.31.5dc9e78e7Fcl7j&id=557200845972&ns=1&abbucket=16#detail'

