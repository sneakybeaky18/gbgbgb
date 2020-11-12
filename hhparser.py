from lxml import html
import requests
import pandas as pd

######################################################################################################################################################

# Необходимо собрать информацию о вакансиях на вводимую должность (используем input или через аргументы) с сайтов Superjob и HH.
# Приложение должно анализировать несколько страниц сайта (также вводим через input или аргументы). Получившийся список должен содержать в себе минимум:

# * Наименование вакансии.
# * Предлагаемую зарплату (отдельно минимальную, максимальную и валюту).
# * Ссылку на саму вакансию.
# * Сайт, откуда собрана вакансия.
#
# По желанию можно добавить ещё параметры вакансии (например, работодателя и расположение).
# Структура должна быть одинаковая для вакансий с обоих сайтов. Общий результат можно вывести с помощью dataFrame через pandas.

######################################################################################################################################################

class ParserHH:

    def get_connection(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
        response = requests.get("https://hh.ru/search/vacancy?st=searchVacancy&text=%D0%9F%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C&area=1&salary=&currency_code=RUR&only_with_salary=true&experience=doesNotMatter&order_by=relevance&search_period=0&items_on_page=50&no_magic=true&L_save_area=true",
                                headers=headers)
        root = html.fromstring(response.text)

        name = root.xpath('//a[@class="bloko-link HH-LinkModifier"]/text()')
        money_raw = root.xpath('//span[@class="bloko-section-header-3 bloko-section-header-3_lite"]/text()')
        link = root.xpath('//a[@class="bloko-link HH-LinkModifier"]/@href')

        # data = root.xpath('//div[@class="bloko-gap bloko-gap_s-top bloko-gap_m-top bloko-gap_l-top"]'
        #                   '//div[@class="vacancy-serp-item "]//a[@class="bloko-link HH-LinkModifier"]'
        #                   '//span[@class="bloko-section-header-3 bloko-section-header-3_lite"]/text()')

        df = {'monthIncome': [], 'JobName': [], 'link': [], 'resource_link': []}
        df = pd.DataFrame(df)

        df['monthIncome'] = money_raw
        df['JobName'] = name
        df['link'] = link
        df['resource_link'] = 'hh.ru'

        df.to_csv('df.csv', index=False)

        return df

pr = ParserHH()

print(pr.get_connection())

print("ok")
