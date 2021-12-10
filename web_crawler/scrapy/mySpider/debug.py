from scrapy import cmdline


cmdline.execute("scrapy crawl itcast".split())

# 将爬取的信息保存到指定格式的文件中，支持的文件格式有：json, jsonlines, jl, csv, xml, marshal, pickle
# cmdline.execute("scrapy crawl itcast -o teachers.xml".split())
