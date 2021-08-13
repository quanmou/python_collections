import os
from pymongo import MongoClient

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MyspiderPipeline:
    def process_item(self, item, spider):
        return item


class TxtPipeline:
    """
    将数据保存为txt，需要在settings.py中设置: 'mySpider.pipelines.TxtPipeline': 300
    """
    def process_item(self, item, spider):
        # 获取当前工作路径
        base_dir = os.getcwd()
        filename = base_dir + "/news.txt"
        with open(filename, 'a') as f:
            f.write(item['name'] + '\n')
            f.write(item['title'] + '\n')
            f.write(item['info'] + '\n\n')

        return item


class MongoPipeline:
    """
    将数据保存到mongoDB中，需要在settings.py中设置: 'mySpider.pipelines.MongoPipeline': 300
    """

    def __init__(self):
        self.db_client = MongoClient()  # 默认连接'mongodb://127.0.0.1:27017'
        self.db = self.db_client["test"]  # 如果不存在名为test的数据库，会自动创建

    def process_item(self, item, spider):
        item = dict(item)
        self.db.teachers.insert_one(item)  # 如果不存在名为teachers的表，会自动创建

        return item
