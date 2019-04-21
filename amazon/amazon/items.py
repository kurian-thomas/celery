# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):
    # define the fields for your item here like:
    pr_name = scrapy.Field()
    pr_tag = scrapy.Field()
    pr_price = scrapy.Field()
    pr_imagelink = scrapy.Field()
    pass
