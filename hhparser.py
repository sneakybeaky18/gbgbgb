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

        linked = input(str("Укажите название вакансии, которые вы ищите: "))

        for el in linked:
            if el == " ":
                linked = input(str("Нужно указать только одну вакансию, без пробелов: "))

        if len(linked) > 15:
            linked = input(str("Нужно указать только одну вакансию: "))

        linked = str("https://hh.ru/search/vacancy?area=1&clusters=true&enable_snippets=true&search_field=name&text=" + str(linked) + "&only_with_salary=true&from=cluster_compensation&showClusters=true")
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}

        response = requests.get(linked,
                                headers=headers)
        root = html.fromstring(response.text)

        name = []
        money_raw = []
        link = []

        money_raw_fixed = []

        links = [linked]

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


        df = {'monthIncome': [], 'JobName': [], 'link': [], 'resource_link': []}
        df = pd.DataFrame(df)

        df['monthIncome'] = money_raw
        df['JobName'] = name
        df['link'] = link
        df['resource_link'] = 'hh.ru'

        df.to_csv('df.csv', index=False)

        return df


pr = ParserHH()

print(pr.get_connection()["monthIncome"])
