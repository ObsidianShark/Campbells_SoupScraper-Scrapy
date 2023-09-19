# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CampbellsItem(scrapy.Item):
    # Product info
    image_urls = scrapy.Field()
    images = scrapy.Field()    
    product_name = scrapy.Field()
    product_description = scrapy.Field()  
    category = scrapy.Field()      
    url = scrapy.Field()
    # Spider info
    scraping_date = scrapy.Field()

