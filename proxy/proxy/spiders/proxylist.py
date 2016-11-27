# -*- coding: utf-8 -*-
import scrapy
from proxy.items import ProxyItem

class ProxylistSpider(scrapy.Spider):
    name = "proxylist"
    allowed_domains = ["kuaidaili.com"]
    start_urls = ['http://kuaidaili.com']

    def parse(self, response):
    	item = ProxyItem()
    	item["IP"] = response.xpath("//div[@id='index_free_list']/table/tbody/tr/td[@data-title='IP']/text()").extract()
    	item["port_1"] = response.xpath("//div[@id='index_free_list']/table/tbody/tr/td[@data-title='PORT']/text()").extract()
    	item["type_1"] = response.xpath("//div[@id='index_free_list']/table/tbody/tr/td[@data-title='类型']/text()").extract()
    	yield item
        
