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
        article_list = response.css("article")
        if len(article_list) <= 0:
            return
        for article in article_list:
            laptop = LaptopItem()
            link = article.css("a::attr(href)").get()
            full_link = response.urljoin(link)
            laptop["url"] = full_link
            
            request = scrapy.Request(url=full_link, callback=self.parseAndFillLaptopData)
            request.meta["item"] = laptop
            yield request
        
        yield scrapy.Request(url=self.next_page_url(response.url), callback=self.parse)
        
    def next_page_url(self, current_page_url):
        index = max(current_page_url.find("&page="), current_page_url.find("?page="))
        if index < 0:
            raise RuntimeError("Url doesnt contain page parameter, can't calculate next page")
        page_number = ""
        start_index = index+len("&page=")
        end_index = 0
        for i in range(start_index, len(current_page_url)):
            char1 = current_page_url[i]
            if char1 in "0123456789":
                page_number += char1
            else:
                end_index = i
                break
        next_page = int(page_number) + 1 
        next_page_url = current_page_url[0:start_index] + str(next_page) + current_page_url[end_index:]       
        return next_page_url

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
    






