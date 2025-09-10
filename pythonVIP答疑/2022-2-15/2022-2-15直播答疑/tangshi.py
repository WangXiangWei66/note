# coding:utf-8
# author:杨淑娟

from selenium import webdriver
# 有两个网址，  一个有“展示阅读全文”，一个没有
lst=['https://so.gushiwen.cn/shiwenv_f732699835a7.aspx','https://so.gushiwen.cn/shiwenv_922dc011e313.aspx']


for item in lst:  # 遍历列表
    # 创建浏览器对象
    driver = webdriver.Chrome()  # 创建浏览器对象
    driver.get(item) # 打开网页
    divlst=driver.find_elements_by_class_name('contyishang')  # 找到含有内容的div ,可能会找到很多个
    for x in divlst: # 遍历
       # print(x.text)
        if '展开阅读全文 ∨' in x.text: # 判断是否包含链接文本

            kk=driver.find_element_by_link_text('展开阅读全文 ∨') # 找到这样的链接文本

            kk.click()  # 点击这个超链
           # print('xxxx')


    print('--------------------------')