#coding=gbk
'''

注意：本文件暂只能实例一次，所有变量将会全局共享

'''

db=None                 #数据库全局对象
conn=None
dbfile='data.db'     #数据库文件名
createtable=1       

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
        db = sqlite.connect(dbfile,isolation_level=None)    
        db.text_factory = str
        #print(sys.getdefaultencoding())
        reload(sys)
        sys.setdefaultencoding('gbk')
        conn  = db.cursor()
    except:
        print "操作sqlite数据库失败，请确保脚本所在目录具有写权限"
        raise SystemExit

    sql="""
       /* id:     流水号 */
       /* hname:     楼盘名称 */
       /* price:     均价 */
       /* area:     片区 */
       /* city:     省市 */
       /* county:     区县 */
       /* addr:     地址 */
       /* type:     建筑类型 */
       /* class:     物业类别 */
       /* right_year:     产权年限 */
       /* right_type:     产权类型 */
       /* gross_area:     建筑面积 */
       /* land_area:     占地面积 */
       /* direction:     方位 */
       /* huxing_size:     户型面积 */
       /* plot_ratio:     容积率 */
       /* Greening_rate:     绿化率 */
       /* total_homes:     总户数 */
       /* developer:     开发商 */
       /* PM_fee:     物业费 */
       /* metro:     轨道沿线/地铁 */
       /* start_date:     开工时间 */
       /* comp_date:     竣工时间 */
       /* open_date:     开盘时间 */
       /* avail_time:     入住时间 */
       /* parking:     车位数 */

        CREATE TABLE IF NOT EXISTS  `house` (
            `id` varchar(20) NOT NULL default '',    
            `hname` varchar(30) NOT NULL default '',    
            `price` varchar(30) NOT NULL default '',
            `area` varchar(30) NOT NULL default '',
            `city` varchar(30) NOT NULL default '',
            `county` varchar(30) NOT NULL default '',
            `addr` varchar(300) NOT NULL default '',
            `type` varchar(30) NOT NULL default '',
            `class` varchar(30) NOT NULL default '',
            `right_year` varchar(30) NOT NULL default '',
            `right_type` varchar(30) NOT NULL default '',
            `gross_area` varchar(30) NOT NULL default '',
            `land_area` varchar(30) NOT NULL default '',
            `direction` varchar(30) NOT NULL default '',
            `huxing_size` varchar(30) NOT NULL default '',
            `plot_ratio` varchar(30) NOT NULL default '',
            `Greening_rate` varchar(30) NOT NULL default '',
            `total_homes` varchar(30) NOT NULL default '',
            `developer` varchar(30) NOT NULL default '',
            `PM_fee` varchar(30) NOT NULL default '',
            `metro` varchar(30) NOT NULL default '',
            `start_date` varchar(30) NOT NULL default '',
            `comp_date` varchar(30) NOT NULL default '',
            `open_date` varchar(30) NOT NULL default '',
            `avail_time` varchar(30) NOT NULL default '',
            `parking` varchar(30) NOT NULL default '',

          PRIMARY KEY (`id`)                    /*  主键 */
        );
        /*
        CREATE INDEX IF NOT EXISTS `area`        ON proxier(`area`);
        CREATE INDEX IF NOT EXISTS `county`   ON proxier(`county`);
        CREATE INDEX IF NOT EXISTS `type`       ON proxier(`type`);
        CREATE INDEX IF NOT EXISTS `class`      ON proxier(`class`);
        */
        PRAGMA encoding = "utf-8";      /* 数据库用 utf-8编码保存 */
    """
    if createtable:
        conn.executescript(sql)
    

    
def add_to_db(item):
    sql="""insert into `house` (
        `id`
        ,`hname`
            ,`price`
            ,`area`
            ,`city`
            ,`county`
            ,`addr`
            ,`type`
            ,`class`
            ,`right_year`
            ,`right_type`
            ,`gross_area`
            ,`land_area`
            ,`direction`
            ,`huxing_size`
            ,`plot_ratio`
            ,`Greening_rate`
            ,`total_homes`
            ,`developer`
            ,`PM_fee`
            ,`metro`
            ,`start_date`
            ,`comp_date`
            ,`open_date`
            ,`avail_time`
            ,`parking`
        ) values
    ('"""
    for i in range(len(item)):
        sql += item[i]+","

    sql += "')"
    try:
        conn.execute(sql)
    except:
        pass 
        