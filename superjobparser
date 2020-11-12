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

class ParserSuperJOB:

    def get_connection(self):

        linked = input(str("Укажите ссылку на вакансии: "))

        #Example
        #https://www.superjob.ru/vakansii/stroitel.html?geo%5Bt%5D%5B0%5D=4

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}

        response = requests.get(linked, headers=headers)
        root = html.fromstring(response.text)

        job_links = root.xpath('//div[@class="_3mfro PlM3e _2JVkc _3LJqf"]//a/@href')
        full_job_links = []

        monthIncomeList = []
        jobnameList = []


        for el in job_links:
            fixed = str("https://www.superjob.ru") + str(el)
            full_job_links.append(fixed)
            # if len(full_job_links) == 3:
            #     break

        for el in full_job_links:
            response = requests.get(el,
                                    headers=headers)
            root = html.fromstring(response.text)

            monthIncome = root.xpath('//span[@class="_1OuF_ ZON4b"]//span/text()')
            monthIncomeList.append(monthIncome)
            JobName = root.xpath('//h1[@class="_3mfro rFbjy s1nFK _2JVkc"]/text()')
            for el in JobName:
                jobnameList.append(el)




        links = ["https://www.superjob.ru/vakansii/programmist.html?geo%5Bt%5D%5B0%5D=4"]


        df = {'monthIncome': [], 'JobName': [], 'link': [], 'resource_link': []}
        df = pd.DataFrame(df)

        df['monthIncome'] = monthIncomeList
        df['JobName'] = jobnameList
        df['link'] = full_job_links
        df['resource_link'] = 'www.superjob.ru'

        df.to_csv('df.csv', index=False)

        print(len(monthIncomeList))
        print(len(jobnameList))

        return jobnameList,monthIncomeList

pr = ParserSuperJOB()

print(pr.get_connection())
