# coding=gbk

import sys

proxy_array=[]          # 代理列表 
db=None                 #数据库全局对象
conn=None
#dbfile='../blog/proxy/proxier0224.db'     #数据库文件名

def open_database():
    global db,conn,dbfile

    try:
        from pysqlite2 import dbapi2 as sqlite
    except:
        print """
        本程序使用 sqlite 做数据库来保存数据，运行本程序需要 pysqlite的支持
        python 访问 sqlite 需要到下面地址下载这个模块 pysqlite,  272kb
        http://initd.org/tracker/pysqlite/wiki/pysqlite#Downloads
        下载(Windows binaries for Python 2.x)
        """
        raise SystemExit

    try:
        '''
        db = sqlite.connect(dbfile,isolation_level=None)    
        db.text_factory = str
        reload(sys)
        sys.setdefaultencoding('gbk')
        #db.create_function("unix_timestamp", 0, my_unix_timestamp)  
        conn  = db.cursor()
        '''
        from django.db import connection
        conn = connection.cursor()
    except:
        print "--blog/proxy.py > 操作sqlite数据库失败，请确保脚本所在目录具有写权限"
        raise SystemExit


def find_proxy ():
    open_database()

    sql = "select ip,port from proxier where active = 1 "
    conn.execute(sql)
    #print sql
    rows = conn.fetchall()   
    #conn.close()
    return rows


def UnitTest ():
    rows = find_proxy()
    print rows[0]


#UnitTest()