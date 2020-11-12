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

        linked = input(str("Укажите ссылку на вакансии с зарплатами: "))

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
        response = requests.get(linked,
                                headers=headers)
        root = html.fromstring(response.text)

        name = []
        money_raw = []
        link = []

        links = [linked]

######################################################################################################################################################
#
# Можно указать набор ссылок со страницами, тогда скрипт их запарсит (если раскоментировать links ниже и закоментировать выше, он спарсит 5 страниц)
#
######################################################################################################################################################


#       links = ["https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&no_magic=true&only_with_salary=true&text=%D0%9F%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C&page=1",
#                "https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&no_magic=true&only_with_salary=true&text=%D0%9F%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C&page=2",
#                "https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&no_magic=true&only_with_salary=true&text=%D0%9F%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C&page=3",
#                "https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&no_magic=true&only_with_salary=true&text=%D0%9F%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C&page=4",
#                 "https://hh.ru/search/vacancy?L_is_autosearch=false&area=1&clusters=true&enable_snippets=true&no_magic=true&only_with_salary=true&text=%D0%9F%D0%B5%D1%80%D1%81%D0%BE%D0%BD%D0%B0%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9+%D0%B2%D0%BE%D0%B4%D0%B8%D1%82%D0%B5%D0%BB%D1%8C&page=5"]


        for el in links:
            response = requests.get(el, headers=headers)
            root = html.fromstring(response.text)
            name_1 = root.xpath('//a[@class="bloko-link HH-LinkModifier"]/text()')
            for el in name_1:
                name.append(el)
            money_raw_1 = root.xpath('//span[@class="bloko-section-header-3 bloko-section-header-3_lite"]/text()')
            for el in money_raw_1:
                money_raw.append(el)
            link_1 = root.xpath('//a[@class="bloko-link HH-LinkModifier"]/@href')
            for el in link_1:
                link.append(el)

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
