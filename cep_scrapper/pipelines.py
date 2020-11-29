# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
from datetime import datetime

from itemadapter import ItemAdapter


class CepScrapperPipeline:
    def open_spider(self, spider):
        today = datetime.today().strftime('%d-%m-%Y')
        self.file = open(f'scrapped-ceps-{today}.jsonl', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
