# -*- coding: utf-8 -*-
import scrapy
from first.items import FirstItem

class CsSpider(scrapy.Spider):
    name = "cs"
    allowed_domains = ["csdn.net"]
    start_urls = (
        'http://blog.csdn.net/',
    )

    def parse(self, response):
        item=FirstItem()
        #item["title"]=response.xpath("/html/head/title/text()").extract()
        item["title"]=response.xpath("//h3[@class='tracking-ad']/a/text()").extract()
        item["detail"]=response.xpath("//div[@class='blog_list_c']/text()").extract()
        item["link"]=response.xpath("//h3[@class='tracking-ad']/a/@href").extract()
        yield item
