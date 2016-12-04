# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ProxyPipeline(object):
    def process_item(self, item, spider):
        for j in range(0,len(item["IP"])):
        	print("IP:"+item["IP"][j])
        	print("端口号："+item["PORT"][j])
        	print("类型："+item["TYPEE"][j])
        	print("---------------------------")
        	with open("list.txt","a") as f:
                    f.write(item["IP"][j])
                    f.write("\n")
                    f.write(item["PORT"][j])
                    f.write("\n")
                    f.write(item["TYPEE"][j])
                    f.write("\n")
                    f.write("-----------------------\n")
                    f.close()
        	
        return item
