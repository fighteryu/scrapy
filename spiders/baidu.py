# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem

class BaiduSpider(scrapy.Spider):
    name = "baidu"
    allowed_domains = ["baidu.com"]
    start_urls = (
        'http://www.baidu.com/',
    )

    def parse(self, response):
        item=FirstItem()
        item["title"]=response.xpath("/html/head/title/text()").extract()
        #print(item["title"])
        yield item
