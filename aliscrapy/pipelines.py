# # -*- coding: utf-8 -*-

# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo

# class AliscrapyPipeline(object):
#     def process_item(self, item, spider):
#         return item

# class MongoDBPipeline(object):

#     def __init__(self):
#         connection = pymongo.MongoClient(
#             settings['MONGODB_SERVER'],
#             settings['MONGODB_PORT']
#         )
#         db = connection[settings['MONGODB_DB']]
#         self.collection = db[settings['MONGODB_COLLECTION']]

#     def process_item(self, item, spider):
#         for data in item:
#             if not data:
#                 raise DropItem("Missing data!")
#         self.collection.update({'url': item['url']}, dict(item), upsert=True)
#         log.msg("Question added to MongoDB database!",
#                 level=log.DEBUG, spider=spider)
#         return item
import json
class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('demo.json', 'w', encoding='utf8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item


