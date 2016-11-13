# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FirstPipeline(object):
    def process_item(self, item, spider):
        #print(item["title"])
        for i in range(0,len(item["title"])):
            print("第"+str(i+1)+"篇文章：")
            print(item["title"][i])
            print(item["detail"][i])
            print(item["link"][i])
            print("------")
        return item
