def get_cookie(url):
    """
    获取该的可用cookie
    :param url:
    :return:
    """

    domain = urllib2.splithost(urllib2.splittype( )[1])[0]
    domain_list = ['.' + domain, domain]
    if len(domain.split('.')) > 2:
        dot_index = domain.find('.')
        domain_list.append(domain[dot_index:])
        domain_list.append(domain[dot_index + 1:])

    conn = None
    cookie_str = None
    try:
        conn = sqlite3.connect(r'%s\Google\Chrome\User Data\Default\Cookies' % os.getenv('LOCALAPPDATA'))
        cursor = conn.cursor()
        print '-' * 50
        sql = 'select host_key, name, value, encrypted_value, path from cookies where host_key in (%s)' % ','.join(['"%s"' % x for x in domain_list])
        row_list = cursor.execute(sql).fetchall()
        print u'一共找到 %d 条' % len(row_list)
        print '-' * 50
        print u'%-20s\t%-5s\t%-5s\t%s' % (u'域', u'键', u'值', u'路径')
        cookie_list = []
        for host_key, name, value, encrypted_value, path in row_list:
            decrypted_value = win32crypt.CryptUnprotectData(encrypted_value, None, None, None, 0)[1].decode(print_charset) or value
            cookie_list.append(name + '=' + decrypted_value)
            print u'%-20s\t%-5s\t%-5s\t%s' % (host_key, name, decrypted_value, path)
        print '-' * 50
        cookie_str = '; '.join(cookie_list)
    except Exception:
        raise CookieException()
    finally:
        conn.close()
        return cookie_str, domain