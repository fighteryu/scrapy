# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyPipeline(object):
    def process_item(self, item, spider):
    	for i in range(0,len(item["IP"])):
    		print("IP:"+item["IP"][i])
    		print("PORT:"+item["port_1"][i])
    		print("类型:"+item["type_1"][i])
    		print("———————————————————————")
    	#print(item["IP"])
    	#print(item["port_1"])
    	#print(item["type_1"])
        #return item
