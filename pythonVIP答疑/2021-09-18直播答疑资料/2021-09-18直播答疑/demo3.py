# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait#显示等待
from selenium.webdriver.support import expected_conditions as ec#等待的条
from selenium.webdriver.common.keys import Keys
import openpyxl
import time

lst = []
wb = openpyxl.Workbook()
driver = webdriver.Chrome()
def login():
    index_url = "https://weibo.com/u/6067480188/home"
    driver.maximize_window()  # 浏览器最大化
    driver.get("https://weibo.com/#_loginLayer_1627384130835")
    WebDriverWait(driver, 100).until(
        ec.url_to_be(index_url)
    )
    print("登录成功")

def Fan():
    driver.find_element_by_class_name("W_input").send_keys("邓紫棋")
    driver.find_element_by_class_name("W_input").send_keys(Keys.ENTER)
    driver.find_elements_by_xpath('//p/span/a')[0].click()
    driver.implicitly_wait(100)

    # 这步找不到数据
    urls = driver.find_elements_by_xpath('//*[@class="info_name W_fb W_f14"]/a[@class="S_txt1"]')

    print(len(urls))
    for url in urls:
        print(url)




def start():
    login()
    Fan()

if __name__ == '__main__':
    start()
