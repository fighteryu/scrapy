# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import urllib.request
#import re

class NituPipeline(object):
    def process_item(self, item, spider):
    	for n in range(0,len(item["url"])):
    		urlpage = item["url"][n]
    		file="E:/百货商场/img/"+urlpage[-18:]
    		urllib.request.urlretrieve(urlpage,filename=file)
    	return item
