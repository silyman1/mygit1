# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeiboItem(scrapy.Item):

    title = scrapy.Field()

    reviewurl = scrapy.Field()

    time_record = scrapy.Field()
