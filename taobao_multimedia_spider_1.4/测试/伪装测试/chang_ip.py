def change_ip(self):
    new_sec = time.time()
    self.sec = new_sec - self.old_sec
    if self.sec > 0:
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
        print proxyMeta
        proxies = {
            "http": proxyMeta,
            "https": proxyMeta,
        }
        self.proxy = proxies
    else:
        self.proxy = self.proxy
