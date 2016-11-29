# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from nitu.items import NituItem

class NipicSpider(scrapy.Spider):
    name = "nipic"
    allowed_domains = ["nipic.com"]
    start_urls = ['http://nipic.com/']

    def parse(self, response):
        url0 = response.xpath("//div[@class='fl nav-item-wrap']//a/@href").extract()
        #url0 = url0[1:4]
        for i in range(0,len(url0)):
        	pageurl0 = url0[i]
        	pageurl0 = response.urljoin(url0[i])
        	#urljoin意义，还有点小用处^_^
        	#print(pageurl0)
        	yield Request(url = pageurl0,callback = self.next)
    #获取第二层链接地址
    
    def next(self,response):
    	url1 = response.xpath("//dd[@class='menu-item-list clearfix']//a/@href").extract()
    	for j in range(0,len(url1)):
    		pageurl1 = url1[j]
    		pageurl1 = response.urljoin(url1[j])
    		#print(pageurl1)	
    		yield Request(url = pageurl1,callback = self.next1)
    #获取第三层链接地址
    def next1(self,response):
    	url2 = response.xpath("//div[@class = 'common-page-box mt10 align-center']//a/@href").extract()
    	#取最后一个网址以此来获取总页码数
    	url2_0 = response.urljoin(url2[-1])
    	#用=分割成两部分字符串
    	url2_0_0 = url2_0.split('=')
    	url2_1 = url2_0_0[0]
    	url2_2 = url2_0_0[1]
    	for k in range(1,int(url2_2)+1):
    		pageurl2 = url2_1 + '=' + str(k)
    		#print(pageurl2)	
    		yield Request(url = pageurl2,callback = self.next2)
    #获取每个图片的地址
    def next2(self,response):
    	item = NituItem()
    	#print(pageurl2)
    	item["url"] = response.xpath("//a[@class='relative block works-detail hover-none works-img-box']//img/@src").extract()
    	yield item
    	