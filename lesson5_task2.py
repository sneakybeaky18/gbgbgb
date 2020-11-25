
from selenium.webdriver.chrome.options import Options
from pymongo import MongoClient
from selenium import webdriver


class Parser:
    def find_and_add_to_db(self):
        chrome_options = Options()
        chrome_options.add_argument('start-maximized')
        driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)

        driver.get('https://www.mvideo.ru/')
        button = driver.find_element_by_xpath(
            "//a[@class='next-btn c-btn c-btn_scroll-horizontal c-btn_icon i-icon-fl-arrow-right']")
        for i in range(3):
            button.click()

        bestsellers = driver.find_element_by_xpath("//div[text()[contains(.,'Хиты продаж')]]/../../../..")
        goods = bestsellers.find_elements_by_css_selector('li.gallery-list-item')
        goods_list = []
        for good in goods:
            goods_dict = {}
            good_name = good.find_element_by_css_selector(
                'a.sel-product-tile-title') \
                .get_attribute('innerHTML')
            goods_dict['good_name'] = good_name
            goods_list.append(goods_dict)

        client = MongoClient('127.0.0.1', 27017)
        db = client['Mvideo']
        goods_collection = db.goods_collection
        goods_collection.insert_many(goods_list)


cc = Parser()
cc.find_and_add_to_db()
