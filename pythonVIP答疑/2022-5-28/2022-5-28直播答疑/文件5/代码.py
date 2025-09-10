from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#构造浏览器
chrome=webdriver.Chrome()
url='https://www.sciencedirect.com'
chrome.get(url)
#chrome.find_element_by_name('pub').send_keys('remote sensing of environment')
chrome.find_element(by=By.NAME,value='pub').send_keys('remote sensing of environment')

#点击搜索按钮
#chrome.find_elements_by_class_name('button')[0].click()#.click()
chrome.find_element(by=By.CLASS_NAME,value='button').click() # 可以根据<button>的class获取按钮

#源代码
html=chrome.page_source
#print(html)
time.sleep(20)

#退出浏览器
chrome.quit()