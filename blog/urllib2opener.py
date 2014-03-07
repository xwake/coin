#coding=gbk
import proxy as prx
import sys,random
import urllib2

proxy_urls = []
debug = 1
def url_proxy_open( url ):
    global proxy_urls
    #随机分配一个代理服务器
    if len(proxy_urls) == 0 :
        proxy_urls = prx.find_proxy()
    
    if len(proxy_urls) == 0 :
        return
    
    ramdom_indexs = range( 0,len(proxy_urls) )
    ramdom_idx = random.sample(ramdom_indexs, 1)
    ramdom_proxy = proxy_urls[ramdom_idx[0]]
    proxy_url = ramdom_proxy[0]+':'+str(ramdom_proxy[1])
    #print proxy_url

    proxy_support = urllib2.ProxyHandler({"http": proxy_url})
    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
    if debug:
        print  '--urllib2opener.py > ',url
    r = urllib2.Request( url )
    
    r.add_header("User-Agent", "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9.1) Gecko/20090624 Firefox/3.5" )
    #r.add_header("Accept", "text/plain" )
    #r.add_header("Accept-Language","zh-cn")   
    #r.add_header("Content-Type","text/html; charset=gb2312")
    content = ''
    try:
        content = opener.open(r).read()
        if debug:
            print '--urllib2opener.py > content.len:',len(content)
    except urllib2.HTTPError, e:  
        #print "Error Code:", e.code, 
        #print '   ,url:', proxy_url 
        pass
    except urllib2.URLError, e:  
        #print "Error Code:", e, 
        #print '    ,url:', proxy_url 
        pass
    except Exception,e:
        #print "Error Reason:",e.code, 
        #print '    ,url:', proxy_url 
        pass
    return content