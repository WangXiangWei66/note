# coding:utf-8
# author:杨淑娟
# selenium 是一个第三方库，需要安装才能使用 pip install selenium  (Python自动化测试时使用的最多)
from selenium import webdriver
from selenium.webdriver.common.by import By

#下载一个谷歌浏览器的驱动   chromedriver.exe ,放到与python.exe文件相同的目录中
driver=webdriver.Chrome()    # 创建谷歌浏览器的对象

#  相当于使用谷歌浏览器去打开网址
driver.get('http://pass.xiang5.com/login.php')

# 定位id输入 框  -->用户名


username=driver.find_element(By.ID,'username')
# 定位id的输入 框-->密码
pwd=driver.find_element(By.ID,'password')

username.send_keys('python1')  # 在用户名的输入 框中输入 用户名 "python1"

pwd.send_keys('123456')   # 在密码的输入 框 中输入 密码  "123456"
driver.find_element(By.CLASS_NAME,'ligin_btn').submit()  # 点击登录按钮

