from pprint import pprint
from lxml import html
import requests
from datetime import datetime
from pymongo import MongoClient


class MailRu_NewsParser:

    def parse(self):

        link = "https://news.mail.ru/"
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
        response = requests.get(link)

        dom = html.fromstring(response.text)

        items = dom.xpath("//div[contains(@class, 'daynews__item')]")

        news_list = []
        currentday = str(datetime.date(datetime.now()))
        for item in items:
            news = {}
            news_name = item.xpath(".//span[contains(@class,'photo__title')]/text()")
            news_link = item.xpath(".//a/@href")

            for link in news_link:
                connection = requests.get(link)
                dom = html.fromstring(connection.text)
                news_date_time = dom.xpath("//span[contains(@class,'note__text breadcrumbs__text js-ago')]/@datetime")
                news_source = dom.xpath("//a[contains(@class,'link color_gray')]//span[@class='link__text']//text()")
                news['datetime'] = news_date_time
                news['news_source'] = news_source

            # news_date_time = item.xpath(".//span[contains(@class,'mg-card-source__time')]/text()")
            # news_source = item.xpath(".//span[@class='mg-card-source__source']//text()")

            news['news_link'] = news_link
            news['news_header'] = news_name
            news_list.append(news)

        return news_list

    def get_db(self):
        client = MongoClient('127.0.0.1', 27017)
        db = client["mail_ru_news"]
        news_collection = db.vacancies_collection
        news_collection.insert_many(self.parse())

cc = MailRu_NewsParser()
pprint(cc.get_db())
