import json
import scrapy


class StradivariusSpider(scrapy.Spider):
    name = 'stradivarius'
    allowed_domains = ['stradivarius.com/tr/en']
    start_urls = ['https://www.stradivarius.com/itxrest/2/catalog/store/54009571/50331081/category?languageId=-1&typeCatalog=1&appId=1']

    def parse(self, response):
        print(response.body)
        data = json.loads(response.body)
        yield from data['categories']['0']['subcategories']['0']['subcategories']
