from pprint import pprint
from lxml import html
import requests
from datetime import datetime
from pymongo import MongoClient


class Yandex_News_Parser:

    def parse(self):

        yandex_news = "https://yandex.ru/news/"
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        response = requests.get(yandex_news)

        dom = html.fromstring(response.text)

        items = dom.xpath("//article[contains(@class, 'mg-card news-card')]")

        news_list = []
        currentday = str(datetime.date(datetime.now()))
        for item in items:
            news = {}
            news_name = item.xpath(".//h2[contains(@class,'news-card__title')]/text()")
            news_link = item.xpath(".//a/@href")
            news_date_time = item.xpath(".//span[contains(@class,'mg-card-source__time')]/text()")
            news['news_link'] = news_link
            news['news_header'] = news_name
            news['datetime'] = str(datetime.date(datetime.now()))
            news['time_gmt3'] = news_date_time
            news_list.append(news)

        return news_list

    def get_db(self):
        client = MongoClient('127.0.0.1', 27017)
        db = client["yandex_news"]
        news_collection = db.vacancies_collection
        news_collection.insert_many(self.parse())

cc = Yandex_News_Parser()
cc.get_db()
