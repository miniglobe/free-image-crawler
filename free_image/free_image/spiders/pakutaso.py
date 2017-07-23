# -*- coding: utf-8 -*-
import scrapy


class PakutasoSpider(scrapy.Spider):
    name = 'pakutaso'
    allowed_domains = ['www.pakutaso.com']
    start_urls = ['https://www.pakutaso.com/']
    
    def parse(self, response):
        anchors = response.css("a")

        image_urls = [anchor.css("a::attr(href)").extract_first() for anchor in anchors if anchor.css("a::attr(data-category)").extract()]
        for image_url in image_urls:
            yield scrapy.Request(image_url, callback=self.parse_dir_contents)

        next_pages = [anchor.css("a::attr(href)").extract_first() for anchor in anchors if not anchor.css("a::attr(data-category)").extract()]
        
        for next_page in next_pages:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, callback=self.parse)
    
    def parse_dir_contents(self, response):
        items = FreeImageItem()
        return items
