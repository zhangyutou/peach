import pymysql


def startdb(sql,method):
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='newpwd',
        db='peach',
        charset='utf8',
        # autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
    )
    cur = conn.cursor()  #建立游标
    if method=='get':
        cur.execute(sql)  #查询数据
        t=cur.fetchall()[0][0]    #获取结果
        print('t=%s' % t)
        return t
    cur.close()     #关闭游标
    conn.close()    #关闭连接




def getPassword(valuename,table,keyname,key):
    sql='select %s from %s where %s="%s";' % (valuename,table,keyname,key)
    result=startdb(sql,'get')
    print('result:%s' % result)
    return result

# passwd = getPassword('password', 'user', 'name', 'zhang')



