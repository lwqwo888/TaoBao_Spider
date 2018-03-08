# -*- coding:utf-8 -*-

import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# 此项目主要参考链接【http://cuiqingcai.com/1076.html，感谢作者的分享

__author__ = 'JustFantasy'



# 模拟登录淘宝类
# 登录淘宝流程
# 1、请求地址https://login.taobao.com/member/login.jhtml获取到token
# 2、请求地址https://passport.alibaba.com/mini_apply_st.js?site=0&token=1L1nkdyfEDIA44Hw1FSDcnA&callback=callback 通过token换取st
# 3、请求地址https://login.taobao.com/member/vst.htm?st={st}实现登录
class Taobao:

    # 初始化方法
    def __init__(self):
        # 登录的URL，获取token
        self.request_url = 'https://login.taobao.com/member/login.jhtml'
        # 通过st实现登录的URL
        self.st_url = 'https://login.taobao.com/member/vst.htm?st={st}'
        # 用户中心地址
        self.user_url = 'https://i.taobao.com/my_taobao.htm'
        # 代理IP地址，防止自己的IP被封禁
        self.proxy_ip = 'http://120.193.146.97:843'
        # 登录POST数据时发送的头部信息
        self.request_headers =  {
            'Host':'login.taobao.com',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Referer' : 'https://login.taobao.com/member/login.jhtml',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection' : 'Keep-Alive'
        }
        # 用户名
        self.username = 'xxx@xxx.com'
        # ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
        self.ua = '089#6o5vOJvX+p/vyJ+evvvvv964Zx59o/eBpRDo3gsRlVypemTq+lp56psnhm5sL5/TvRMoZ//llHppexSA/99V6N9d3uCs5+K+v+7akvvvyFmNxoT5G0y/ZdMM6m0mGJlo3kJi5J5vR/EKvvvwb9ghRluiJwlHYHN43dhi+x5rYx0kvlvesIJvvxprxNge+hXxpxKzcV8iKq05ZuT03LK+v+7akvvvyFbFxoT5G0y/ZdMM6m0mGJlo3kJi5J5vR/EKvvvwDhjhRluiJwlHYHN43dhi+x5rYx0Vvlv5CtGNMx8+v+uMO/p9uE2COPovypleYeYY+8KOYBJ+v+24FVhTZxriDpLjmSNDWm8AHc7PEBUsV+QPdu8+v+uMX/p9kLpCOPovZ5ZhYK7goZKOYoK+v+paZNvvy/oCxoT5GXSR6V0wYV/zGJkDvlv62X0xkt96vJ3GZv5vaVNMkud3Breg/VynptGv2p22kFpOhIxbKNMiEpJVvlv5CtGNMYv+vvLasgQ1nG7xyYN+vveBZ6C4Q7NTvlv0vvVKd+kpyxlvvKgK96/PiJvvmNJ/7uLMvvVhV+kp35lvvKgK96/jscv+v1pFSd/wMWE5lVlbVHkBypEe3sElZuQA/pUrRTM49uspFuplpn4BypEe3sE36zDIFvg7l5v2Sm+usv6lO9QoSIsv6v5QKoDb9l6d/R6a7LJVEmjl/x5wz791bs2c6LVQ+lKs19IVSHr1/meeV4YPy+/V879d5W/I9l6d/Qv+7LDvln7KVmI87NJ68wDFK6lQaJ5spRJlXLvV+Qpusk5SZ7lpepvF/oVQ+l6Lv5TQZXgpv46s85QQRvKRy97t5XglvJpTKv5BR68Rlx27ukTl7J/x5HKsKsOpvNenposw7eeu+ula5HvOM/s56wlbZsQBFwDG/v2Gcmpk/uJQsHJI9pwp37L+ZoQBFwDjup+GMz95FuM5pHDIa95+csIQ3+O/+NpmQoI27oDaa4+3875oKPSxDsDeWuQw97gdpL7SSmLp9dpvlV4fZ9y5v7+0pWRPs5vTvs8m9ojpv46l8TbQRv6fhL+lZuQA/pUrRTM45689vL9gFlYPc7Uky7TY8zDI9l6d/QKsSulpv46s8vRQ9N+Vb/JYhsdFVv7mpoDJ7+8bvs9/O+VX5vK9epy9KkIHp+p7/+Eu5689v45vks8Hzo/V879Jse88vJ8IQFMkzovV+QlJvuZ87Jev34pyYsVQ+lZuKL5L92/x+4EF9aQp77Z9yvDuK+X0vlvclvVxCdouvJKEQnkGvlvRrGGorJLYnJ5v+RyBvlQDvlv62X09kjS6vJhSnv5vVOOXa5AOklKxxeN+vv44XdwY8TTVvHfDvlv62X04kTL6vJyy3v5vR4eEVSHChn2oQ9qrPv6LYNu+ABESRI0W+DRtvJ5v+cGqMcvfvlv/tY79sQf7WfSglx+xxHd61ZuVRdMVvlv5CtGNMx8+v+uMO/p9es6COPovZ5ZhYK7goZKOYNK+vvkqCtVNyJ5v93o2s/pYv4Uz15vNlNg0dFB5NL0zyJ5v93H2s/pYvRUz15vwp+T2T009JL0z3v5vR4eDRGljhn2oQK32P+oAydtKAFEPhw5K9Wb6vJ5v+cGqMcvkvlvesIJvvxpBWNge+hXxpxKzcV8iKq05ZuT03JK+vvkqCtVN5J5vR/EKvvvwDtghRluiJwlHYHN43dhi+x5rYx0kvlvesIJvvxpIZlge+hXxpxKzcV8iKq05ZuT03LK+v+7akvvvyFEPxoT5G0y/ZdMM6m0mGJlo3kJi5J5vR/EKvvvwEdghRluiJwlHYHN43dhi+x5rYx0kvlvesIJvvxpt8vge+hXxpxKzcV8iKq05ZuT03mJ+v+24FWuTUBriDpdpXUNV8kT5AM/n1oSYRNF+AN=='
        # 密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
        self.password2 = '98d8979ad859f27838ba5aa299217fb4edf7b46f052c1330bf9fe57d594a09e5ee9402fc9bb86d83d9c0d5b50b13e93a8679e2699a17a87993d435e25ac81b01c74d68a3eb6460b0a1e05068d337567be980911e0dcaa6ef2b8141aeb21cf547c8a77c2aa9ff6ea724e6f2df838c3680cf56ba8e0484da15051bdd27eaee5a20'
        self.post = {
            'ua': self.ua,
            'TPL_checkcode': '',
            'CtrlVersion': '1,0,0,7',
            'TPL_password': '',
            'TPL_redirect_url': 'http://i.taobao.com/my_taobao.htm',
            'TPL_username': self.username,
            'loginsite': '0',
            'newlogin': '0',
            'from': 'tb',
            'fc': 'default',
            'style': 'default',
            'css_style': '',
            'tid': 'XOR_1_000000000000000000000000000000_625C4720470A0A050976770A',
            'support': '000001',
            'loginType': '4',
            'minititle': '',
            'minipara': '',
            'umto': 'NaN',
            'pstrong': '3',
            'llnick': '',
            'sign': '',
            'need_sign': '',
            'isIgnore': '',
            'full_redirect': '',
            'popid': '',
            'callback': '',
            'guf': '',
            'not_duplite_str': '',
            'need_user_id': '',
            'poy': '',
            'gvfdcname': '10',
            'gvfdcre': '',
            'from_encoding ': '',
            'sub': '',
            'TPL_password_2': self.password2,
            'loginASR': '1',
            'loginASRSuc': '1',
            'allp': '',
            'oslanguage': 'zh-CN',
            'sr': '1366*768',
            'osVer': 'windows|6.1',
            'naviVer': 'firefox|35'
        }
        # 将POST的数据进行编码转换
        self.post_data = urllib.parse.urlencode(self.post).encode(encoding='GBK')
        # 设置代理
        self.proxy = urllib.request.ProxyHandler({'http': self.proxy_ip})
        # 设置cookie
        self.cookie = http.cookiejar.LWPCookieJar()
        # 设置cookie处理器
        self.cookieHandler = urllib.request.HTTPCookieProcessor(self.cookie)
        # 设置登录时用到的opener，它的open方法相当于urllib2.urlopen
        self.opener = urllib.request.build_opener(self.cookieHandler, self.proxy, urllib.request.HTTPHandler)
        # 赋值J_HToken
        self.J_HToken = ''
        # 登录成功时，需要的Cookie
        self.newCookie = http.cookiejar.CookieJar()
        # 登陆成功时，需要的一个新的opener
        self.newOpener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.newCookie))

    # 利用st码进行登录
    # 这一步我是参考的崔庆才的个人博客的教程，因为抓包的时候并没有抓取到这个url
    # 但是如果不走这一步，登录又无法成功
    # 区别是并不需要传递user_name字段，只需要st就可以了
    def login_by_st(self, st):
        st_url = self.st_url.format(st=st)
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Host':'login.taobao.com',
            'Connection' : 'Keep-Alive'
        }
        request = urllib.request.Request(st_url, headers=headers)
        response = self.newOpener.open(request)
        content =  response.read().decode('gbk')

        #检测结果，看是否登录成功
        pattern = re.compile('top.location.href = "(.*?)"', re.S)
        match = re.search(pattern, content)
        print(match)
        if match:
            print(u'登录网址成功')
            return True
        else:
            print(u'登录失败')
            return False


    # 程序运行主干
    def main(self):
        try:
            # 请求登录地址， 此时返回的页面中有两个js的引入
            # 位置是页面的前两个JS的引入，其中都带有token参数
            request = urllib.request.Request(self.request_url, self.post_data, self.request_headers)
            response = self.opener.open(request)
            content = response.read().decode('gbk')

            # 抓取页面中的两个获取st的js
            pattern = re.compile('<script src=\"(.*)\"><\/script>')
            match = pattern.findall(content)

            # [
            # 'https://passport.alibaba.com/mini_apply_st.js?site=0&token=1f2f3ePAx5b-G8YbNIlDCFQ&callback=callback',
            # 'https://passport.alipay.com/mini_apply_st.js?site=0&token=1tbpdXJo6W1E4bgPCfOEiGw&callback=callback',
            # 'https://g.alicdn.com/kissy/k/1.4.2/seed-min.js',
            # 'https://g.alicdn.com/vip/login/0.5.43/js/login/miser-reg.js?t=20160617'
            # ]
            # 其中第一个是我们需要请求的JS，它会返回我们需要的st
            #print(match)


            # 如果匹配到了则去获取st
            if match:
                # 此时可以看到有两个st， 一个alibaba的，一个alipay的，我们用alibaba的去实现登录
                request = urllib.request.Request(match[0])
                response = urllib.request.urlopen(request)
                content = response.read().decode('gbk')

                # {"code":200,"data":{"st":"1lmuSWeWh1zGQn-t7cfAwvw"} 这段JS正常的话会包含这一段，我们需要的就是st
                #print(content)

                # 正则匹配st
                pattern = re.compile('{"st":"(.*?)"}')
                match = pattern.findall(content)

                # 利用st进行登录
                if match:
                    self.login_by_st(match[0])
                else:
                    print(u'无法获取到st，请检查')
                    return

                # 请求用户中心，查看打印出来的内容，可以看到用户中心的相关信息
                response = self.newOpener.open(self.user_url)
                page = response.read().decode('utf-8')
                print(page)

        except urllib.error.HTTPError as e:
            print(u'请求失败，错误信息：', e.msg)



taobao = Taobao()
taobao.main()

