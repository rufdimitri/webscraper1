# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyProject1Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LaptopItem(scrapy.Item):
    title = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()
    cpu = scrapy.Field()
    graphics = scrapy.Field()
    storage_type = scrapy.Field()
    storage = scrapy.Field()
    weight = scrapy.Field()
