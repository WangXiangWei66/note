# coding:utf-8
# author:杨淑娟
from selenium import  webdriver

driver=webdriver.Chrome() # 创建谷歌的驱动

driver.get('http://www.baidu.com')

# 执行js代码
js='window.alert("你好，欢迎访问百度")'  # 最简单的JS代码

driver.execute_script(js)

