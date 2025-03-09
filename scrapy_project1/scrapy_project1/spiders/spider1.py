import scrapy
from Include.config1 import Config

from scrapy_project1.items import LaptopItem


class Spider1Spider(scrapy.Spider):
    base_url = Config.spider1["domain_url"]
    url = base_url + "/search-results/?price=389-924&page=1&tile_type=electronics&page_type=category&category=2&sort_by=score"
    
    name = "spider1"
    allowed_domains = Config.spider1["allowed_domains"]
    start_urls = [url]



    def parse(self, response):
        print(f"response-url: {response.url}")
        print(f"response-status: {response.status}")
        article_list = response.css("article")
        for article in article_list:
            laptop = LaptopItem()
            link = article.css("a::attr(href)").get()
            full_link = response.urljoin(link)
            laptop["link"] = full_link
            laptop["price"] = "0"
            
            request = scrapy.Request(url=full_link, callback=self.parseAndFillLaptopData)
            request.meta["item"] = laptop
            yield request
            break #DEBUG only parse for 1st laptop 


    def parseAndFillLaptopData(self, response):
        laptop = response.meta["item"]

        laptop["title"] = response.css('#wrapper > div > section > div > div > div > div > div > div > h1 > span[data-test="product-name"]::text').get().strip()

        laptop["price"] = response.css('#wrapper > div > section > div > div > div > div > div > div > div > div > div > p[data-test="product-price"] > span::text').get()
        
        table_rows = response.css('#tab-spezifikationen > dl > div[data-test="details-attribute"]')
        for row in table_rows:
            attribute = row.css('dt::text').get().strip()
            value = row.css('dd::text').get().strip()
            if "Grafikkarte" == attribute:
                laptop["graphics"] = value
            if "Prozessor" == attribute:
                laptop["cpu"] = value
            if "Festplattenart" == attribute: 
                laptop["storage_type"] = value
            if "Speicherplatz" == attribute:
                laptop["storage"] = value
            if "Gewicht" == attribute:
                laptop["weight"] = value
        
        yield laptop
    






