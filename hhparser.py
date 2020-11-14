from lxml import html
import re
import requests
import pandas as pd
import numpy as np

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

    def data_convert(self):

        # data = "df.csv"
        # df = pd.read_csv(data)
        df = self.get_connection()
        list = df['monthIncome']
        list2 = []

        for el in list:
            filter1 = el.replace(u'\xa0',"")
            filter2 = filter1.replace(" ","")
            filter3 = filter2.replace(u"\n2","")
            filter4 = filter3.replace("от","")
            filter5 = filter4.replace(".","")
            list2.append(filter5)
        df = df.drop(columns=['monthIncome'])

        minMaxValues = []
        for el in list2:
            r = re.findall(r"([\d|\s]+)", str(el))
            minMaxValues.append(r)

        df['money'] = minMaxValues

        maxValues = []
        minValues = []
        for money in df['money']:
            minValues.append(money[0])
            maxValues.append(money[-1])

        df['min_money'] = minValues
        df['max_money'] = maxValues

        df = df.drop(columns=['money'])

        df.to_csv('df_corrected.csv', index=False)

        return df

pr = ParserHH()

# pr.get_connection()
print(pr.data_convert())
