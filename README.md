# scrapy

# 流程:分析网站---->决定爬取方式和策略---->创建项目---->定义items---->编写爬虫、pipelines、settings---->debug



# items.py 定义爬取内容
# pipelines.py 数据爬取后处理
# settings.py 项目设置文件（用户代理、cookie等）不遵循robots协议
# scrapy.cfg  配置文件

# scrapy crawl --nolog


# xpath http://www.w3school.com.cn/xpath/
# /  提取标签   
# text() 提取文本信息   
# //  寻找所有标签  
# @  提取属性   //link[@属性 = 属性值]


# spilt用法

>>> u = "www.doiido.com.cn"  
#使用默认分隔符
>>> print u.split()
['www.doiido.com.cn']  
#以"."为分隔符
>>> print u.split('.')
['www', 'doiido', 'com', 'cn']  
#分割0次
>>> print u.split('.',0)
['www.doiido.com.cn']  
#分割一次
>>> print u.split('.',1)
['www', 'doiido.com.cn']  
#分割两次
>>> print u.split('.',2)
['www', 'doiido', 'com.cn']  
#分割两次，并取序列为1的项
>>> print u.split('.',2)[1]
doiido  
#分割最多次（实际与不加num参数相同）
>>> print u.split('.',-1)
['www', 'doiido', 'com', 'cn']  
#分割两次，并把分割后的三个部分保存到三个文件
>>> u1,u2,u3 = u.split('.',2)
>>> print u1www
>>> print u2doiido
>>> print u3com.cn

# urljoin()用法

urllib.parse.urljoin(base, url, allow_fragments=True)
>>>Construct a full (“absolute”) URL by combining a “base URL” (base) with another URL (url). Informally, this uses components of the >>>base URL, in particular the addressing scheme, the network location and (part of) the path, to provide missing components in the >>>relative URL.

from urllib.parse import urljoin
urljoin('http://www.cwi.nl/%7Eguido/Python.html', 'FAQ.html')
'http://www.cwi.nl/%7Eguido/FAQ.html'


#scrapy 日志文件保存
>>scrapy crawl spder_name -s LOG_FILE=scrapy.log 
