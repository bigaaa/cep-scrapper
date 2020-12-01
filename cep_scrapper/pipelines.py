# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json
import os
from datetime import datetime


class CepScrapperPipeline:
    def open_spider(self, spider):
        today = datetime.today().strftime('%d-%m-%Y')
        os.makedirs('output', exist_ok=True)
        self.file = open(f'output/scrapped-ceps-{today}.jsonl', 'w', encoding='utf-8')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
