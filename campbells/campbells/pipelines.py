# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import pymongo
import logging
from scrapy.utils.project import get_project_settings
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem

# class MongoDBPipeline:
    
#     def __init__(self):
#         settings = get_project_settings()
#         connection = pymongo.MongoClient(
#             settings['MONGODB_SERVER'],
#             settings['MONGODB_PORT']
#         )
#         db = connection[settings['MONGODB_DB']]
#         self.collection = db[settings['MONGODB_COLLECTION']]

#     def process_item(self, item, spider):
#         adapter = ItemAdapter(item)
#         if adapter.get("image_urls"):
#             self.collection.insert_one(dict(item))
#             # logging.INFO("Product added to MongoDB database!")
#             return item
#         else: 
#             raise DropItem(f"Missing images in {item}")
