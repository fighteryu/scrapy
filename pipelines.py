# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#piplines 文件用于数据的后处理，需要开启setting文件的piplines
class FirstPipeline(object):
    def process_item(self, item, spider):
        for i in range(0,len(item["title"])):
            print("第"+str(i+1)+"篇文章：")
            print(item["title"][i])
            print(item["detail"][i])
            print(item["link"][i])
            print("------")
        return item
