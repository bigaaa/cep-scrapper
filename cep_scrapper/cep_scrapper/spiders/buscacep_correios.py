import re
from uuid import uuid4

import scrapy
from scrapy import FormRequest

from cep_scrapper.items import CepScrapperItem


class BuscacepCorreiosSpider(scrapy.Spider):
    name = 'buscacep_correios'
    allowed_domains = ['buscacep.correios.com.br']
    start_urls = ['http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm']

    def parse(self, response):
        ufs = response.xpath('//select/option/text()').getall()[1:]
        for uf in ufs:
            yield FormRequest.from_response(response, formdata={'UF': uf}, callback=self.get_cep)

    def get_cep(self, response):
        uf = re.findall(r'(?<=UF=)\S{2}', str(response.request.body))[0]
        table = response.xpath('//tr[count(td)=4]')
        next_page_link = response.xpath('//form[@name="Proxima"]/following-sibling::*/@href').get()

        for row in table:
            columns = row.xpath('./td/text()').getall()
            new_item = CepScrapperItem(id=str(uuid4()), uf=uf, locality=columns[0],
                                       cep_range=columns[1], status=columns[2], range_type=columns[3])
            yield new_item

        if next_page_link:
            yield FormRequest.from_response(response, formname='Proxima', callback=self.get_cep)

