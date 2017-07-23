# -*- coding: utf-8 -*-
import scrapy


class PakutasoSpider(scrapy.Spider):
    name = 'pakutaso'
    allowed_domains = ['https://www.pakutaso.com/']
    start_urls = ['http://https://www.pakutaso.com//']

    def parse(self, response):
        pass
