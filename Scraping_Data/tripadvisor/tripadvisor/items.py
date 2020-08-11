# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TripadvisorItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    author_comment = scrapy.Field()
    author_address = scrapy.Field()
    title_comments = scrapy.Field()
    body_comments = scrapy.Field()
    date_comments = scrapy.Field()
