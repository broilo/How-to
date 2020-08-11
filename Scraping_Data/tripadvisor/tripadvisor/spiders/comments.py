# -*- coding: utf-8 -*-
import scrapy
from ..items import TripadvisorItem

class CommentsSpider(scrapy.Spider):
    name = 'comments'
    allowed_domains = ['tripadvisor.com.br']
    start_urls = ['https://www.tripadvisor.com.br/Attraction_Review-g775227-d554708-Reviews-Parque_Estadual_do_Caracol-Canela_State_of_Rio_Grande_do_Sul.html']

    def parse(self, response):
        item = TripadvisorItem()
        box_of_comments = response.xpath("//div[@class='Dq9MAugU T870kzTX LnVzGwUB']")
        for box in box_of_comments:
            item["author_comments"] = box.xpath(".//div[@class='_2fxQ4TOx']/span/a/text()']").get()
            item["author_address"] = box.xpath(".//span[@class='default _3J15flPT small']/text()").get()
            item["title_comments"] = box.xpath(".//div[@class='glasR4aX']/a//span/text()").get()
            item["body_comments"] = box.xpath(".//div[@class='cPQsENeY']/q/span/text()").get()
            item["date_comments"] = box.xpath(".//span[@class='_34Xs-BQm']/text()").get()
            yield item
           
            
