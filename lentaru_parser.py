from pprint import pprint
from lxml import html
import requests
from datetime import datetime
from pymongo import MongoClient
import re


class LentaRu_Parser:

    def parse(self):

        link = "https://lenta.ru/parts/news/"
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        response = requests.get(link)

        dom = html.fromstring(response.text)

        items = dom.xpath("//div[contains(@class,'news')]")

        news_list = []
        currentday = str(datetime.date(datetime.now()))
        for item in items:
            news = {}

            news_link = item.xpath(".//h3//a/@href")
            posting_time = item.xpath(".//div[contains(@class,'item')]/text()")
            header = item.xpath('.//h3//a/text()')

            news['news_link'] = news_link
            news['posting_time'] = posting_time
            news['news_header'] = header
            news['news_source'] = "https://lenta.ru/parts/news/"

            news_list.append(news)

        return news_list

    def get_db(self):
        client = MongoClient('127.0.0.1', 27017)
        db = client["mail_ru_news"]
        news_collection = db.vacancies_collection
        news_collection.insert_many(self.parse())



###########################
# Пока что без обработки пропусков
# её добавить не сложно, но пока что
# нету на это полноценно времени
###########################

cc = LentaRu_Parser()
pprint(cc.parse())
