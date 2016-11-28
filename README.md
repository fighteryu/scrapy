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