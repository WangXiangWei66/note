# coding:utf-8
# 教育机构：马士兵教育
# 讲    师：杨淑娟

#使用Python，把html中的两个文本框添入值
#使用到的第三方模块selenium
from selenium import webdriver
#创建一个谷歌浏览器对象
driver=webdriver.Chrome()
#自动打开一个网页
driver.get('http://127.0.0.1:8020/HelloHBuilder/myfile.html')
#获取第一个文本框
input1=driver.find_element_by_id('wd') # 根据id获取网页元素  获取HTML页面上的第一个文本框
input2=driver.find_element_by_id('username') # 根据id获以网页，获取的是HTML页面上的第二个文本框

#使用js代码向两个文本框中填入值
#使用python去执行js代码
#driver.execute_script('arguments[0].value="{0}"'.format('ysj'),input1,input2) # 值会有哪个框中出现

driver.execute_script('arguments[1].value="{0}"'.format('杨淑娟'),input1,input2)
# 格式化字符中的方式 %s
driver.execute_script('arguments[0].value="%s"' % 'ysj',input1,input2)




