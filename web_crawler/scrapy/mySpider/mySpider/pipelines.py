import os

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
