#------------middleare.py文件---------------------#
#下载中间件
#导入随机数模块
import random
from wx.settings import IPPOOL
#导入官方代理IP的一个模块
from scrapy.contrib.downloadermiddleware.httpproxy import HttpProxyMiddleware
class IPPOOLS(HttpProxyMiddleware):
    def __init__(self,ip=''):
        self.ip=ip
    def process_request(self, request, spider):
        thisip=random.choice(IPPOOL)
        print("当前使用的IP是"+thisip["ipaddr"])
        try:
            request.meta["proxy"]="http://"+thisip["ipaddr"]
        except Exception as e:
            pass           
            
 #----------seethings文件配置------------------------#
 #加入IP代理池
 IPPOOL=[
    {"ipaddr":"127.0.0.1:8888"},
    {"ipaddr":"106.120.78.129:80"},
]
 #加入download_middlewares
 DOWNLOADER_MIDDLEWARES = {
    #'wx.middlewares.MyCustomDownloaderMiddleware': 543,
    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 123,
    'wx.middlewares.IPPOOLS': 125#优先级，执行顺序
}
