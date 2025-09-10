# coding:utf-8
# author:杨淑娟
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.baidu.com')
# 定位id输入 框
     #  find_element_by_id()这个被弃用的方法，底层使用的就是find_element
inputtag=driver.find_element_by_id('kw') # 删除线，这个方法已经弃用了

inputtag=driver.find_element(By.ID,'kw')

inputtag.send_keys('hello')
