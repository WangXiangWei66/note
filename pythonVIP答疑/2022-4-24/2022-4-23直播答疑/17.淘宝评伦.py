# coding:utf-8
# author:杨淑娟
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time,json
import requests
driver = webdriver.Chrome()
driver.maximize_window()
url = 'https://item.taobao.com/item.htm?id=625517236169&ali_refid=a3_430582_1006:1169480187:N:%2Fwsr5MERvsuHaBaBYVbB9kS1C4TtwQRN:ee4edf56848b0e22601005a944283c65&ali_trackid=1_ee4edf56848b0e22601005a944283c65&spm=a230r.1.14.6#detail'
driver.get(url)
time.sleep(15)
driver.get(url)
# buy = driver.find_element_by_xpath('//div[@class="tb-btn-buy"]/a')
# time.sleep(2)
action = ActionChains(driver)
evaluate = driver.find_element_by_xpath('//div[@class="tb-shop-info-ft"]/a[1]')
# input = driver.find_element_by_xpath('//input[@class="search-combobox-input"]')
# ActionChains(driver).move_to_element(buy).click(buy).click()
time.sleep(2)
action.move_to_element_with_offset(evaluate,1,1).click(evaluate).perform()#可能为坐标反爬下·
# ActionChains(driver).move_to_element(input).click(input).click()
# input.send_keys('牛奶')
