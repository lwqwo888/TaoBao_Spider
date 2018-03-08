def aaa():
    for i in ggg:
        print i

if __name__ == '__main__':
    ggg = 'hkjasdlbao'
    aaa()
    sql = u"insert into erp_cat_status(track_number,status_label,date_at) VALUES (%s,%s,%s) " % (1,2,3)
    print sql
