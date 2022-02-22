import scrapy

class NewSpider(scrapy.Spider):
    name="new_spider"
    start_urls = ["http://192.168.1.3/spicyx/"]
    def parse(self, response):
        for every_response in response.css("img"):
            yield{
                "Image Link is": every_response.xpath('@src').extract_first(),
            }