# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    push = scrapy.Field()
    url = scrapy.Field()
    pass
