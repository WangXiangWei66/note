# 还有就是selenium无法正常加载子网页的问题，能打开首页，当点击子页面是为空
import time


from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('start-maximized')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
chrome=webdriver.Chrome(options=options)

chrome.get('https://wenshu.court.gov.cn/')
time.sleep(2)
log_tag=chrome.find_element_by_xpath('//*[@id="loginLi"]/a')
time.sleep(2)
log_tag.click()
