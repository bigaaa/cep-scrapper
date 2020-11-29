# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CepScrapperItem(scrapy.Item):
    id = scrapy.Field()
    uf = scrapy.Field()
    locality = scrapy.Field()
    cep_range = scrapy.Field()
    status = scrapy.Field()
    range_type = scrapy.Field()
