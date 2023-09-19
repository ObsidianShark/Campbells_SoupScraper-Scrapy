import scrapy
import re
from campbells.items import CampbellsItem
from scrapy.loader import ItemLoader
from pathlib import Path
from urllib.parse import urljoin

from itemloaders.processors import MapCompose, TakeFirst, Identity
from datetime import datetime


def remove_unicode(text):
    text = re.sub(r"[\n\t]*", "", text)
    return text

class SoupSpider(scrapy.Spider):
    name = "campbells"
    # allowed_domains = ["campbells.com"]
    start_urls = ["https://www.campbells.com/products/"]
    custom_settings = {
        "AUTOTHROTTLE_ENABLED" : True,
        "AUTOTHROTTLE_DEBUG" : True,
        "HTTPCACHE_ENABLED" : True,
        "DOWNLOAD_DELAY" : 10,
        "FEED_FORMAT" : "csv",
        "FEED_URI" : f"{name}.csv",
        "ITEM_PIPELINES": {'scrapy.pipelines.images.ImagesPipeline': 1},
        "IMAGES_STORE": 'YOUR_PATH',             
    }

    def parse(self, response):
        for product in response.xpath("//a[@class='csc-cards__item']/@href"):
            yield scrapy.Request(url=product.get(), callback=self.parse_product)

        next_page = response.xpath("//a[@class='next page-numbers']/@href").get()
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)

    def parse_product(self, response):
        product = ItemLoader(item=CampbellsItem(), selector=response)
        product.default_input_processor = MapCompose(remove_unicode)
        product.default_output_processor = TakeFirst()
        product.scraping_date_in = MapCompose()
        product.image_urls_in = MapCompose()
        product.image_urls_out = Identity()

        product.add_xpath("image_urls","//li[contains(@class, 'product-gallery__item')]/img/@src")
        product.add_xpath("product_name","//h1[contains(@class, 'product-description__title')]/text()")
        product.add_xpath("product_description","//div[@itemprop='description']/text()")  
        product.add_xpath("category","//div[@class='product-description']/p[1]/text()")              
        
        product.add_value("url", response.request.url)
        product.add_value("scraping_date", datetime.now())

        yield product.load_item()

