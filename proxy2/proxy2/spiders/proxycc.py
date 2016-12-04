# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from proxy.items import ProxyItem

class ProxyccSpider(scrapy.Spider):
    name = "proxycc"
    allowed_domains = ["kuaidaili.com"]
    start_urls = ['http://kuaidaili.com/free/inha']
    """
    def parse(self, response):
      	url0 = response.xpath("//li[@id='menu_free']/a/@href").extract()
      	url0_0 = response.urljoin(url0[0])
      	#print(url0_0)  
      	yield Request(url=url0_0,callback=self.next)

    def next(self,response):
    	url1=response.xpath("//div[@class='tag_area2']/a/@href").extract()
    	url1_1=response.urljoin(url1[0])
    	#print(url1_1)
    	yield Request(url=url1_1,callback=self.next2)
    """
    def parse(self,response):
    	
    	#item = ProxyItem()
    	url2=response.xpath("//div[@id='listnav']//ul//a/text()").extract()
    	url_sum=(url2[-1])
    	#print(url_sum)
    	for i in range(1,int(url_sum)+1):
            urlpage=response.url+'/'+str(i)
            print(urlpage)
            yield Request(url=urlpage,callback=self.next3)

    def next3(self,response):
        item=ProxyItem()
        item["IP"]=response.xpath("//tbody//tr//td[@data-title='IP']/text()").extract()
        item["PORT"]=response.xpath("//tbody//tr//td[@data-title='PORT']/text()").extract()
        item["TYPEE"]=response.xpath("//tbody//tr/td[@data-title='类型']/text()").extract()
        yield item

