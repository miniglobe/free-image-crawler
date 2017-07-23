# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
sys.path.append('./model')
from repository import Repository

class FreeImagePipeline(object):
    def __init__(self):
        self.repository = Repository()

    def process_item(self, item, spider):
        self.repository(item)
        return item
