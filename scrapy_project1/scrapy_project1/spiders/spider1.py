import scrapy

from scrapy_project1.items import LaptopItem


class Spider1Spider(scrapy.Spider):
    name = "spider1"
    allowed_domains = ["TODO local/config.json"]
    start_urls = ["TODO local/config.json"]


    def parse(self, response):
        article_list = response.css("article")
        for article in article_list:
            laptop = LaptopItem()
            link = article.css("a::attr(href)")
            full_link = response.urljoin(link)



